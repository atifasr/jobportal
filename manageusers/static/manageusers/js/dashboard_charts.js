
$(document).ready(
  function(e)
  {
    $.ajax(
      {
        url:'/dashboard_data/',
        method : 'GET',
        dataType: "json",
        contentType: "application/json",
        cache : false,
        success : function(data){
            console.log(data)
        }
      }
    )
  }
)



let ctx = document.getElementById('myChart').getContext('2d');

let myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: 'No of submissions',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        responsive:true,
        maintainAspectRatio :true
    }
});


// pie chart code

let pieChart =  document.getElementById('pieChart').getContext('2d');

const data = {
    labels: [
      'rejected',
      'selected',
      'onhold'
    ],
    datasets: [{
      label: 'No of applicants',
      data: [300, 50, 100],
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)'
      ],
      hoverOffset: 4
    }],
    options: {
        responsive:true,
        maintainAspectRatio :true
    }
  };


const config = {
    type: 'doughnut',
    data: data,
  };



let pie_chart = new Chart(pieChart,config) 


// line chart
let lineGraph = document.getElementById('line_chart').getContext('2d');

const labels = [1,2,3,4,5];
const data2 = {
  labels: labels,
  datasets: [{
    label: 'My First Dataset',
    data: [65, 59, 80, 81, 56, 55, 40],
    fill: false,
    borderColor: 'rgb(75, 192, 192)',
    tension: 0.1
  }]
};


const config2 = {
    type: 'line',
    data: data2,
  };


let lineChart = new Chart(lineGraph,config2) 