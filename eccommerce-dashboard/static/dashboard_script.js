 // Fetch and render orders over time chart
 fetch('/api/orders_over_time')
 .then(response => response.json())
 .then(data => {
     const ctx = document.getElementById('ordersChart').getContext('2d');
     new Chart(ctx, {
         type: 'line',
         data: {
             labels: data.dates,
             datasets: [{
                 label: 'Number of Orders',
                 data: data.counts,
                 borderColor: 'rgba(75, 192, 192, 1)',
                 backgroundColor: 'rgba(75, 192, 192, 0.2)',
                 fill: false
             }]
         },
         options: {
             responsive: true,
             scales: {
                 x: {
                     type: 'time',
                     time: {
                         unit: 'day'
                     }
                 },
                 y: {
                     beginAtZero: true
                 }
             }
         }

     });
 });

// Fetch and render low stock levels chart
fetch('/api/low_stock_levels')
 .then(response => response.json())
 .then(data => {
     const ctx = document.getElementById('stockChart').getContext('2d');
     new Chart(ctx, {
         type: 'bar',
         data: {
             labels: data.products,
             datasets: [{
                 label: 'Stock Quantity',
                 data: data.quantities,
                 backgroundColor: 'rgba(255, 99, 132, 0.2)',
                 borderColor: 'rgba(255, 99, 132, 1)',
                 borderWidth: 1
             }]
         },
         options: {
             responsive: true,
             scales: {
                 y: {
                     beginAtZero: true
                 },
                 x: {
                     display: false  // This will hide the x-axis labels
                 }
             }
         }
     });
 });

// Fetch and render most popular products bar chart
fetch('/api/most_popular_products')
 .then(response => response.json())
 .then(data => {
     const productNames = data.map(item => item.product_name);
     const quantities = data.map(item => item.total_quantity);

     const ctx = document.getElementById('popularProductsChart').getContext('2d');
     new Chart(ctx, {
         type: 'bar',
         data: {
             labels: productNames,
             datasets: [{
                 label: 'Quantity Sold',
                 data: quantities,
                 backgroundColor: 'rgba(75, 192, 192, 0.2)',
                 borderColor: 'rgb(243, 13, 13)',
                 borderWidth: 1
             }]
         },
         options: {
             scales: {
                 y: {
                     beginAtZero: true
                 },
                 x: {
                     display: false  // This will hide the x-axis labels
                 }
             }
         }
     });
 });
 

