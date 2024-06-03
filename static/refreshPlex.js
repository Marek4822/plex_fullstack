function confirmRefresh() {
    if (confirm('Are you sure you want to refresh PLEX?')){
            fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ action: 'refresh' }),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        } else {
            console.log('PLEX refresh canceled!');
        }
    }