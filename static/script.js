
document.addEventListener('DOMContentLoaded', () => {
    const seasonOptions = document.querySelectorAll('.season-option');
  
    function selectSeason(event) {
      const option = event.currentTarget;
      document.getElementById('season').value = option.dataset.label;
      seasonOptions.forEach(option => option.classList.remove('selected'));
      option.classList.add('selected');
    }
  
    // Add event listeners for season options
    seasonOptions.forEach(option => {
      option.addEventListener('click', selectSeason);
    });
  });
  
  
  function selectOption(optionId) {
    // Remove 'selected' class from all options
    document.querySelectorAll('.category-option').forEach(option => {
      option.classList.remove('selected');
    });
  
    // Add 'selected' class to the clicked option
    document.getElementById(optionId).classList.add('selected');
  }
  
  function prevSection() {
    // Logic to navigate to the previous section
  }
  
  function nextSection() {
    // Logic to navigate to the next section
  }
  
  
        document.addEventListener('DOMContentLoaded', () => {
          let currentSection = 0;
          const sections = document.querySelectorAll('.input-section');
          const ageOptions = document.querySelectorAll('.age-option');
          const genderOptions = document.querySelectorAll('.gender-option');
  
          function showSection(index) {
            sections.forEach((section, i) => {
              section.classList.toggle('active', i === index);
            });
          }
  
          function selectAgeRange(event) {
            const option = event.currentTarget;
            document.getElementById('age_range').value = option.dataset.label;
            document.getElementById('age_start').value = option.dataset.start;
            document.getElementById('age_end').value = option.dataset.end;
            ageOptions.forEach(option => option.classList.remove('selected'));
            option.classList.add('selected');
          }
  
          function selectGender(event) {
            const option = event.currentTarget;
            document.getElementById('gender').value = option.dataset.label;
            genderOptions.forEach(option => option.classList.remove('selected'));
            option.classList.add('selected');
          }
  
          function nextSection() {
            if (currentSection < sections.length - 1) {
              currentSection++;
              showSection(currentSection);
              updateButtonVisibility();
            }
          }
  
          function prevSection() {
            if (currentSection > 0) {
              currentSection--;
              showSection(currentSection);
              updateButtonVisibility();
            }
          }
  
          function updateButtonVisibility() {
            document.querySelector('.button-container.first-page').style.display = currentSection === 0 ? 'flex' : 'none';
            document.querySelectorAll('.button-container:not(.first-page)').forEach(container => {
              container.style.display = currentSection === sections.length - 1 ? 'flex' : 'flex';
            });
          }
  
          // Initialize the form
          showSection(currentSection);
          updateButtonVisibility();
  
          // Add event listeners for age options
          ageOptions.forEach(option => {
            option.addEventListener('click', selectAgeRange);
          });
  
          // Add event listeners for gender options
          genderOptions.forEach(option => {
            option.addEventListener('click', selectGender);
          });
  
          // Add event listeners to handle navigation
          document.querySelectorAll('.btn-primary').forEach(button => {
            button.addEventListener('click', nextSection);
          });
  
          document.querySelectorAll('.btn-secondary').forEach(button => {
            button.addEventListener('click', prevSection);
          });
        });
  
