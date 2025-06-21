// Service API Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// Service Management Class
class ServiceManager {
    constructor() {
        this.services = [];
        this.init();
    }

    async init() {
        await this.loadServices();
        this.renderServices();
    }

    async loadServices() {
        try {
            const response = await fetch(`${API_BASE_URL}/services/`);
            const data = await response.json();
            
            if (data.success) {
                this.services = data.services;
            } else {
                console.error('Failed to load services:', data.error);
                this.showError('Failed to load services');
            }
        } catch (error) {
            console.error('Error loading services:', error);
            this.showError('Error loading services');
        }
    }

    renderServices() {
        const container = document.querySelector('.service-collection-list');
        if (!container) {
            console.error('Service container not found');
            return;
        }

        if (this.services.length === 0) {
            container.innerHTML = `
                <div class="service-loading">
                    No services available
                </div>
            `;
            return;
        }

        container.innerHTML = this.services.map(service => this.createServiceCard(service)).join('');
    }

    createServiceCard(service) {
        return `
            <div role="listitem" class="service-collection-item w-dyn-item">
                <a href="service.html" class="service-card is-service w-inline-block">
                    <div class="service-card-image-wrapper is-service">
                        <img loading="lazy" 
                             src="${service.image_path}" 
                             alt="${service.title}"
                             class="service-card-image"/>
                        <div class="service-card-hover-button is-service"></div>
                        <div class="service-card-button-wrapper is-service">
                            <div class="service-card-button is-service">
                                <div class="view-button-text">
                                    View<br/>Details
                                </div>
                                <div class="service-card-arrow-wrapper">
                                    <img loading="lazy" 
                                         src="https://cdn.prod.website-files.com/6759a39683657b8e1facb485/6759a39683657b8e1facc0c2_Service%20Arrow%201.svg" 
                                         alt="" 
                                         class="service-card-arrow"/>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="service-card-content">
                        <h5 class="heading-style-h5">${service.title}</h5>
                    </div>
                </a>
            </div>
        `;
    }

    showError(message) {
        const container = document.querySelector('.service-collection-list');
        if (container) {
            container.innerHTML = `
                <div class="service-error">
                    ${message}
                </div>
            `;
        }
    }

    showLoading() {
        const container = document.querySelector('.service-collection-list');
        if (container) {
            container.innerHTML = `
                <div class="service-loading">
                    Loading services...
                </div>
            `;
        }
    }

    // Admin functions for managing services
    async addService(serviceData) {
        try {
            const response = await fetch(`${API_BASE_URL}/services/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(serviceData)
            });

            const data = await response.json();
            
            if (data.success) {
                await this.loadServices();
                this.renderServices();
                return { success: true, message: 'Service added successfully' };
            } else {
                return { success: false, message: data.error };
            }
        } catch (error) {
            console.error('Error adding service:', error);
            return { success: false, message: 'Error adding service' };
        }
    }

    async updateService(serviceId, serviceData) {
        try {
            const response = await fetch(`${API_BASE_URL}/services/${serviceId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(serviceData)
            });

            const data = await response.json();
            
            if (data.success) {
                await this.loadServices();
                this.renderServices();
                return { success: true, message: 'Service updated successfully' };
            } else {
                return { success: false, message: data.error };
            }
        } catch (error) {
            console.error('Error updating service:', error);
            return { success: false, message: 'Error updating service' };
        }
    }

    async deleteService(serviceId) {
        try {
            const response = await fetch(`${API_BASE_URL}/services/${serviceId}`, {
                method: 'DELETE'
            });

            const data = await response.json();
            
            if (data.success) {
                await this.loadServices();
                this.renderServices();
                return { success: true, message: 'Service deleted successfully' };
            } else {
                return { success: false, message: data.error };
            }
        } catch (error) {
            console.error('Error deleting service:', error);
            return { success: false, message: 'Error deleting service' };
        }
    }
}

// Initialize service manager when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on the service page
    if (document.querySelector('.service-collection-list')) {
        window.serviceManager = new ServiceManager();
    }
});

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ServiceManager;
} 