function changeChart(chartId) {
  const charts = document.getElementsByClassName('chart')
  for (let chart of charts) {
    if(chart.className.includes(chartId)) {
      chart.hidden = false
    }
    else {
      chart.hidden = true
    }
  }
  const buttons = document.getElementsByClassName('chartControl')
  for (let button of buttons) {
    if(button.className.includes(chartId)) {
      button.style.color = 'red'
    }
    else {
      button.style.color = 'black'
    }
  }
}
// const charts = document.getElementsByClassName('chart')
// for (let chart of charts) {
//   if(chart.className.includes('total_')) {
//     chart.hidden = false
//   }
//   else {
//     chart.hidden = true
//   }
// }