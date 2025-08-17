document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl, {
            trigger: 'hover focus'
        });
    });
    
    // Initialize Bootstrap popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
    
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s ease-out';
            alert.style.opacity = '0';
            setTimeout(() => {
                alert.remove();
            }, 500);
        }, 5000);
    });
    
    // Form validation enhancements
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
    
    // Image preview for profile picture upload
    const profilePicInput = document.getElementById('id_profile_pic');
    if (profilePicInput) {
        profilePicInput.addEventListener('change', function(e) {
            const [file] = e.target.files;
            if (file) {
                const preview = document.getElementById('profile-pic-preview');
                preview.src = URL.createObjectURL(file);
                preview.onload = function() {
                    URL.revokeObjectURL(preview.src);
                }
            }
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // Back to top button functionality
    const backToTopButton = document.getElementById('back-to-top');
    if (backToTopButton) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopButton.style.display = 'block';
            } else {
                backToTopButton.style.display = 'none';
            }
        });
        
        backToTopButton.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({top: 0, behavior: 'smooth'});
        });
    }
    
    // Markdown preview toggle (if you implement markdown)
    const markdownToggle = document.getElementById('markdown-toggle');
    if (markdownToggle) {
        const markdownPreview = document.getElementById('markdown-preview');
        const markdownTextarea = document.getElementById('id_content');
        
        markdownToggle.addEventListener('click', function() {
            if (this.textContent === 'Preview') {
                // Convert markdown to HTML (you'll need a markdown library)
                // markdownPreview.innerHTML = marked(markdownTextarea.value);
                markdownPreview.style.display = 'block';
                markdownTextarea.style.display = 'none';
                this.textContent = 'Edit';
            } else {
                markdownPreview.style.display = 'none';
                markdownTextarea.style.display = 'block';
                this.textContent = 'Preview';
            }
        });
    }
    
    // Add active class to current nav link
    const currentUrl = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentUrl) {
            link.classList.add('active');
        }
    });
    
    // Confirm before deleting
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this?')) {
                e.preventDefault();
            }
        });
    });
});
