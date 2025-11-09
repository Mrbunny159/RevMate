document.addEventListener('DOMContentLoaded', () => {
  fetch('/api/rides')
    .then(res => res.json())
    .then(rides => {
      const list = document.getElementById('ride-list');
      rides.forEach(ride => {
        const card = document.createElement('div');
        card.className = 'col-sm-6 mb-3';
        card.innerHTML = `
          <div class="card">
            <div class="card-body">
              <h5>${ride.title}</h5>
              <p>By: ${ride.organizer}</p>
              <p>Date: ${new Date(ride.ride_date).toLocaleString()}</p>
              <a href="<https://maps.google.com/?q=${ride.start_location>[0]},${ride.start_location[1]}" target="_blank">Start Location</a>
              <button class="btn btn-sm btn-primary mt-2" onclick="joinRide('${ride.ride_id}')">Join Ride</button>
            </div>
          </div>
        `;
        list.appendChild(card);
      });
    });
});

function joinRide(ride_id) {
  fetch(`/api/rides/join/${ride_id}`, { method: 'POST', headers: {"Authorization": "Bearer " + getToken()} })
    .then(res => res.json())
    .then(data => {
      if (data.success) alert('Joined ride!');
      else alert('Error joining ride');
    });
}
