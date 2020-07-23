const date = document.querySelector('#date');
date.textContent = new Date().getFullYear();

const clientHeight = document.querySelector('#navbar').offsetHeight;
let showcaseHeight = 0;
let hasShowcase = false;

if (document.querySelector('#header-home') !== null) {
  hasShowcase = true;
}

if (hasShowcase) {
  showcaseHeight = document.querySelector('#header-home').offsetHeight;
}

// Smooth Scroll
$(document).ready(function () {
  $('#navbar a').on('click', function (event) {
    if (this.hash !== '') {
      event.preventDefault();

      const hash = this.hash;

      $('html, body').animate(
        {
          scrollTop: $(hash).offset().top - clientHeight,
        },
        1000
      );
    }
  });
});

// Back to Top
$(window).scroll(function () {
  if ($(this).scrollTop() > 100) {
    $('.back-to-top').fadeIn('slow');
  } else {
    $('.back-to-top').fadeOut('slow');
  }
});
$('.back-to-top').click(function () {
  $('html, body').animate(
    {
      scrollTop: 0,
    },
    1500,
    'easeInOutExpo'
  );
  return false;
});

// Navbar Overlay
window.addEventListener('scroll', () => {
  if (window.scrollY > showcaseHeight - 16) {
    document.querySelector('#navbar').style.backgroundColor =
      'rgba(0, 0, 0, 0.9)';
    // document.querySelector('.back-to-top').style.display = 'block';
  } else {
    document.querySelector('#navbar').style.backgroundColor = 'transparent';
    // document.querySelector('.back-to-top').style.display = 'none';
  }
});

// Typewriter
class TypeWriter {
  constructor(txtElement, words, wait = 3000) {
    this.txtElement = txtElement;
    this.words = words;
    this.txt = '';
    this.wordIndex = 0;
    this.wait = parseInt(wait, 10);
    this.type();
    this.isDeleting = false;
  }

  type() {
    // Current index of word
    const current = this.wordIndex % this.words.length;
    // Get full text of current word
    const fullTxt = this.words[current];

    // Check if deleting
    if (this.isDeleting) {
      // Remove char
      this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
      // Add char
      this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    // Insert txt into element
    this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;

    // Initial Type Speed
    let typeSpeed = 100;

    if (this.isDeleting) {
      typeSpeed /= 2;
    }

    // If word is complete
    if (!this.isDeleting && this.txt === fullTxt) {
      // Make pause at end
      typeSpeed = this.wait;
      // Set delete to true
      this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
      this.isDeleting = false;
      // Move to next word
      this.wordIndex++;
      // Pause before start typing
      typeSpeed = 500;
    }

    setTimeout(() => this.type(), typeSpeed);
  }
}

// Init On DOM Load
document.addEventListener('DOMContentLoaded', init);

// Init App
function init() {
  if (hasShowcase) {
    const txtElement = document.querySelector('.txt-type');
    const words = JSON.parse(txtElement.getAttribute('data-words'));
    const wait = txtElement.getAttribute('data-wait');
    // Init TypeWriter
    new TypeWriter(txtElement, words, wait);
  }
}
