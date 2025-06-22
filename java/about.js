document.addEventListener('DOMContentLoaded', function() {
    const teamListContainer = document.getElementById('team-list');

    if (teamListContainer) {
        fetchTeamMembers();
    }

    function fetchTeamMembers() {
        showLoading();
        fetch('http://localhost:5000/api/team')
            .then(response => response.json())
            .then(data => {
                if (data.success && data.team) {
                    renderTeamMembers(data.team);
                } else {
                    showError('Failed to load team members.');
                }
            })
            .catch(error => {
                console.error('Error fetching team members:', error);
                showError('An error occurred while fetching team members.');
            });
    }

    function renderTeamMembers(members) {
        if (members.length === 0) {
            showError('No team members found.');
            return;
        }

        teamListContainer.innerHTML = members.map(member => createTeamCard(member)).join('');
    }

    function createTeamCard(member) {
        return `
            <div role="listitem" class="team-collection-item w-dyn-item">
                <div class="team-card">
                    <div class="team-card-details">
                        <div class="team-card-content">
                            <h5 class="heading-style-h5">${member.name}</h5>
                            <div class="text-size-regular">${member.role}</div>
                        </div>
                        <div class="team-card-social-wrapper">
                            ${member.facebook_link ? `<a href="${member.facebook_link}" target="_blank" class="team-social-link w-inline-block"><img src="icons/facebook.svg" loading="lazy" alt="Facebook Icon"/></a>` : ''}
                            ${member.instagram_link ? `<a href="${member.instagram_link}" target="_blank" class="team-social-link w-inline-block"><img src="icons/instagram.svg" loading="lazy" alt="Instagram Icon"/></a>` : ''}
                            ${member.twitter_link ? `<a href="${member.twitter_link}" target="_blank" class="team-social-link w-inline-block"><img src="icons/twitter.svg" loading="lazy" alt="Twitter Icon"/></a>` : ''}
                        </div>
                    </div>
                    <div class="team-card-image-wrapper">
                        <img src="${member.image_path}" loading="lazy" alt="${member.name}" class="team-card-image" />
                    </div>
                </div>
            </div>
        `;
    }

    function showLoading() {
        teamListContainer.innerHTML = '<div class="team-loading">Loading Team...</div>';
    }

    function showError(message) {
        teamListContainer.innerHTML = `<div class="team-error">${message}</div>`;
    }
}); 