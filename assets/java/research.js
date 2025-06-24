// Research API integration
const API_BASE_URL = 'http://localhost:5000/api';

// Function to fetch research data from API
async function fetchResearchData() {
    try {
        const response = await fetch(`${API_BASE_URL}/research`);
        const data = await response.json();
        
        if (data.success) {
            displayResearchCards(data.data);
        } else {
            console.error('Error fetching research data:', data.message);
            // Fallback to static content if API fails
            console.log('Using fallback static content');
        }
    } catch (error) {
        console.error('Error fetching research data:', error);
        // Fallback to static content if API fails
        console.log('Using fallback static content');
    }
}

// Function to display research cards
function displayResearchCards(researchData) {
    const researchList = document.querySelector('.research-collection-list');
    
    if (!researchList) {
        console.error('Research list container not found');
        return;
    }
    
    // Clear existing content
    researchList.innerHTML = '';
    
    // Create research cards for each item
    researchData.forEach(research => {
        const researchCard = createResearchCard(research);
        researchList.appendChild(researchCard);
    });
}

// Function to create a research card element
function createResearchCard(research) {
    const listItem = document.createElement('div');
    listItem.role = 'listitem';
    listItem.className = 'research-collection-item w-dyn-item';
    
    const link = document.createElement('a');
    link.href = research.external_link || 'research.html';
    link.className = 'research-card is-research w-inline-block';
    
    if (research.external_link) {
        link.target = '_blank';
        link.rel = 'noopener noreferrer';
    }
    
    link.innerHTML = `
        <div class="research-card-top-content-wrapper">
            <div class="research-card-top-content">
                <div class="text-size-regular">/</div>
                <div class="text-size-regular">${research.category}</div>
                <div class="text-size-regular">/</div>
            </div>
            <div class="text-size-regular text-color-black-900">${research.date}</div>
        </div>
        <div class="research-card-image-wrapper">
            <img loading="lazy" src="${research.image_link}" alt="${research.heading}" 
                 sizes="(max-width: 479px) 86vw, (max-width: 767px) 87vw, (max-width: 991px) 39vw, 524px" 
                 class="research-card-image"/>
        </div>
        <div class="research-card-hover-button"></div>
        <div class="research-card-button-wrapper">
            <div class="research-card-button">
                <div>
                    View<br/>Details
                </div>
                <div class="research-card-arrow-wrapper">
                    <img loading="lazy" src="https://cdn.prod.website-files.com/6759a39683657b8e1facb485/6759a39683657b8e1facc0c2_Service%20Arrow%201.svg" alt="" class="research-card-arrow"/>
                </div>
            </div>
        </div>
        <div class="research-card-content-wrapper">
            <h5 class="heading-style-h5">${research.heading}</h5>
            <p class="text-size-small text-color-black-700">${research.description}</p>
        </div>
    `;
    
    listItem.appendChild(link);
    return listItem;
}

// Function to handle image loading errors
function handleImageError(img) {
    // Fallback to a default image if the specified image fails to load
    img.src = 'assets/research_image/research1.webp';
    img.alt = 'Research Image';
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Fetch and display research data
    fetchResearchData();
    
    // Add error handling for images
    document.addEventListener('error', function(e) {
        if (e.target.tagName === 'IMG') {
            handleImageError(e.target);
        }
    }, true);
});

// Export functions for potential use in other scripts
window.ResearchAPI = {
    fetchResearchData,
    displayResearchCards,
    createResearchCard
}; 