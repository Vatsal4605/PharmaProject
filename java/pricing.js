// pricing.js

document.addEventListener('DOMContentLoaded', () => {
    const API_BASE_URL = 'http://localhost:5000/api';
    const packagesContainer = document.getElementById('pricing-packages-container');
    const tabs = document.querySelectorAll('.price-tab-link');
    let allPackages = [];

    // Fetches pricing data and initializes the view
    async function initializePricing() {
        try {
            const response = await fetch(`${API_BASE_URL}/pricing`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            allPackages = await response.json();
            // Set up click listeners for all tabs
            setupTabs();
            // Find the active tab on load (Basic is marked as current in HTML)
            const activeTab = document.querySelector('.price-tab-link.w--current');
            let defaultPackageName = 'standard'; // Default to standard since it's marked as current
            if (activeTab) {
                defaultPackageName = activeTab.dataset.package;
            }
            // Find the package that matches the default tab
            const defaultPackage = findPackageByName(defaultPackageName);
            if (defaultPackage) {
                displayPackage(defaultPackage);
            } else if (allPackages.length > 0) {
                displayPackage(allPackages[0]); // Fallback to the first package
            }
        } catch (error) {
            console.error("Failed to fetch pricing data:", error);
            if (packagesContainer) {
                packagesContainer.innerHTML = '<p>Error loading pricing information. Please try again later.</p>';
            }
        }
    }
    // Helper function to find package by name
    function findPackageByName(packageType) {
        const packageMap = {
            'standard': 'Standard Package',
            'premium': 'Premium Package',
            'elite': 'Elite Package'
        };
        const fullName = packageMap[packageType];
        return allPackages.find(p => p.name === fullName);
    }
    // Displays a single pricing package
    function displayPackage(pkg) {
        if (!pkg) {
            packagesContainer.innerHTML = '<p>Selected package not found.</p>';
            return;
        }
        packagesContainer.innerHTML = createPackageHTML(pkg);
    }
    // Creates the HTML for a pricing package card
    function createPackageHTML(pkg) {
        const benefitsHTML = (pkg.benefits || []).map(benefit => `
            <div class="benefit-item">
                <img src="icons/tick.svg" loading="lazy" alt="Tick" class="benefit-icon"/>
                <div class="text-size-regular">${benefit}</div>
            </div>
        `).join('');
        return `
            <div class="price-card">
                <div class="price-card-left-content">
                    <h3 class="heading-style-h3">${pkg.name}</h3>
                    <p class="text-size-regular text-color-black-700">${pkg.description}</p>
                    <div class="padding-bottom padding-medium"></div>
                    <div class="price-text">${pkg.price}</div>
                    <div class="padding-bottom padding-large"></div>
                    <a href="${pkg.get_started_link}" class="button w-inline-block">
                        <div class="botton-text">Get Started now</div>
                    </a>
                </div>
                <div class="price-card-right-content">
                    <div class="text-size-large">Benefits Included :-</div>
                    <div class="padding-bottom padding-medium"></div>
                    <div class="benefit-list">${benefitsHTML}</div>
                </div>
            </div>
        `;
    }
    // Sets up the tab functionality
    function setupTabs() {
        tabs.forEach(tab => {
            tab.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                tabs.forEach(t => t.classList.remove('w--current'));
                this.classList.add('w--current');
                const packageName = this.dataset.package;
                const selectedPackage = findPackageByName(packageName);
                displayPackage(selectedPackage);
            });
        });
    }
    // Initial load
    if (packagesContainer && tabs.length > 0) {
        packagesContainer.innerHTML = '<div style="text-align: center; padding: 2rem;"><p>Loading pricing packages...</p></div>';
        initializePricing();
    }
}); 