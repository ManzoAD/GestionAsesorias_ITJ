/* const ctx = document.getElementById('myChart');
 */const names =['Carlos','Pedro','Maria','Rosa','Juan']
const ages = [24,10,54,51,15]

/* const myChart = new Chart(ctx,{
type: 'bar',
data:{
    labels: names,
    datasets:[
        {
        label:'Edad',
        data: ages,
        backgroundColor:[
            rgba(255,99,132,0.2),
            rgba(54,162,235,0.2),
            rgba(255,206,86,0.2),
            rgba(75,192,192,0.2),
            rgba(153,102,255,0.2),
            rgba(255,159,64,0.2)
        ],
        borderColor: [
            rgba(255,99,132,1),
            rgba(54,162,235,1),
            rgba(255,206,86,1),
            rgba(75,192,192,1),
            rgba(153,102,255,1),
            rgba(255,159,64,1)
        ],
        borderWith: 1.5
    }]
}
}); */
/* 
const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: 'Evaluacion Asesoria',
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor:[
            '#ef0808','#0094FF','#f0e21c','#2fff00','#7909ba','#ef6808'
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  }); */

  const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      
      labels: ['Horario', 'Tecnicas', 'Temas', 'Organizado', 'Dudas', 'Academico','Conocimientos'],
      datasets: [{
        label: 'Evaluacion Asesoria',
        data: [60, 75, 80, 88, 90,94 ,100],
        backgroundColor:[
            '#ef0808','#0094FF','#f0e21c','#2fff00','#7909ba','#ef6808','#0dbcae'
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          title:{
            display:true,
            text:'(%) Efectividad'
          }
        }
      }
    }
  });