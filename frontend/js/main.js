// For handling auth modals, storing JWT, API calls (example)
function saveToken(token) {
  localStorage.setItem('jwt', token);
}
function getToken() {
  return localStorage.getItem('jwt');
}
// Example: Fetch user
async function fetchUser() {
  const token = getToken();
  if (!token) return;
  const res = await fetch('/api/user', {
    headers: {"Authorization": "Bearer " + token}
  });
  if (res.ok) {
    const user = await res.json();
    // Render user data
  }
}
