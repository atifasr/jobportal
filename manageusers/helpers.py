
from concurrent import futures
import requests
from bs4 import BeautifulSoup
from requests.api import request
from concurrent.futures import ThreadPoolExecutor
from job_management.models import JobPost
from companyprofile.models import Company
import time
import decimal

#for setting connection and getting soup obj
def get_content(page_no=0):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
    url = f"https://in.indeed.com/jobs?q=work+from+home&start=10"

    resp = requests.get(url,headers=headers)
    print(resp.status_code)
    soup = BeautifulSoup(resp.content, 'html.parser')
    
    return soup

# indeed job descriptions using links 

def get_job_detail(job_link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
    url = f"https://in.indeed.com{job_link}"
    resp = requests.get(url,headers=headers)
    resp = BeautifulSoup(resp.content,"html.parser")
    job = resp.find("div",class_ = "jobsearch-JobComponent")
    job_body = job.find("div",class_ = "jobsearch-jobDescriptionText")
    job_description = job_body.find_all("p")
    for value in job_description:
        print(value.get_text())

    



#getting job links
def get_links(content):
    job_links = content.find_all("a",class_ = "tapItem")
    job_link_list = []
    for links in job_links:
        job_link_list.append(links['href']) 
    get_job_detail(job_link_list[0])



 
#modifying salary part
def modify_salary(salary_str):
    salary={
        
    }
    salary_start,salary_end = salary_str.rstrip(" a month").rstrip(" a year").split("-")
    salary['salary_start']=salary_start
    salary['salary_end']=salary_end
    return salary
 
       
    


#getting job data dictionary
def get_data(soup):
    job_links = soup.find_all("a",class_ = "tapItem")

    content = soup.find_all("table",class_ = "jobCard_mainContent")
    job_descrip = soup.find_all("table",class_ ="jobCardShelfContainer")
    job_details_list = []
    for val,descrip,links in zip(content,job_descrip,job_links):
        semi_descript = descrip.find("div",class_ = "job-snippet")
        date_ = descrip.find("span",class_ = "date")

        result_content  = val.find_all("td",class_ = "resultContent")
        for result in result_content:
            try:
                descrip = semi_descript.find("ul").get_text()
            except:
                descrip = None
            job_date = date_.get_text()


            job_title = result.find("h2",class_= "jobTitle").get_text()
            company_name = result.find("span",class_ = "companyName").get_text()
            company_location = result.find("div",class_ = "companyLocation").get_text()
            job_detail ={
                'job_title':job_title,
                'company_name':company_name,
                'company_location':company_location,  
                'job_descrip':descrip,
                'job_posted_date':job_date,
                'job_link':f"https://in.indeed.com{links['href']}"
            }
            try:
                salary = result.find("span", class_ = "salary-snippet").get_text()
                job_detail['salary'] = modify_salary(salary)
            except Exception as e:
                salary = 0
            
            job_details_list.append(job_detail)

    return job_details_list








def push_data():
    
    executor = ThreadPoolExecutor(max_workers=3)
    content_future = executor.submit(get_content)
    print('waiting on job data')
    time.sleep(1)
    content = content_future.result()
    future = executor.submit(get_data,content)
    job_details = future.result()
    
    job_post_list=[]
    for ins in job_details:
        try:
            salary_strt = ins['salary']['salary_start']
            salary_end = ins['salary']['salary_end']
            salary_start = float(salary_strt.lstrip("₹").replace(",","").strip(" "))
            salary_end = float(salary_end.lstrip(" ₹").replace(",","").strip(" "))
            print(salary_start,salary_end)
        except:
            salary_start = salary_end = 0

        company,created = Company.objects.get_or_create(
            name__iexact = ins['company_name'],defaults={
                "name":ins['company_name']
            }
        )

        job_post_list.append(
            JobPost(
            title = ins['job_title'],
            cmpny_name = company,
            job_description = ins['job_descrip'],
            direct_link = ins['job_link'],
            salary_start = salary_start,
            salary_end = salary_end
        ) 
        )
    JobPost.objects.bulk_create(job_post_list)
    print('job data pushed')
        

    

