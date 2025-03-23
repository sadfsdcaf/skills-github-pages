fetch('output.json')  // Updated to fetch from the same directory
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok ' + response.statusText);
    }
    return response.json();
  })
  .then(data => {
    const table = document.getElementById('data-table');
    const labels = [];
    const values = [];

    data.results.forEach(item => {
      labels.push(item.label);
      values.push(item.value);
      const row = `<tr><td>${item.label}</td><td>${item.value}</td></tr>`;
      table.insertAdjacentHTML('beforeend', row);
    });

    const ctx = document.getElementById('chart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Values',
          data: values,
        }]
      }
    });
  })
  .catch(error => console.error('Error loading JSON:', error));
