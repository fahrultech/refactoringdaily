const dBlogApp = function() {
  const selectors = {
     body: document.querySelector('body'),
    menuIcon: document.getElementById('menu-animate-icon'),
    mobileNav: document.querySelector('.mobile-nav'),
    searchIcon: document.querySelector('.header-top-search-btn'),
    searchForm: document.getElementById('search-form'),
    headerNav: document.querySelector('.header-nav'),
    mobileMenu: document.getElementById('mobile-menu'),
    filterAmountItems: document.querySelectorAll('.filter-item').length,
    filterMenuItem: document.querySelectorAll('.menu-filter li'),
    filterMenuLink: document.querySelectorAll('.menu-filter li a'),
    emptyFilter: document.querySelector('.filter-empty'),
    filterItem: document.querySelectorAll('.filter-item'),
    postSlider: document.querySelector('.post-slider'),
    shopItems: document.querySelectorAll('.shop-item'),
    portfolioItems: document.querySelectorAll('.portfolio-item'),
    portfolioAmountItems: document.querySelector('.portfolio-amount-items'),
    shopAmoutItems: document.querySelector('.shop-amount-items'),
    writeResponseBtn: document.querySelector('.write-a-response-btn'),
    responseFormWrapper: document.querySelector('.response-form-wrapper'),
    commentResponse: document.querySelectorAll('.comment-response'),
    showMoreAnswersBtn: document.querySelector('.show-more-answers'),
    showMoreAnswersBtnText: document.querySelector('.show-more-answers-text'),
    hideMoreAnswersBtnText: document.querySelector('.hide-more-answers-text'),
  }
  const debounce = (func, wait, immediate) => {
    var timeout;
    return function() {
      var context = this, args = arguments;
      var later = function() {
        timeout = null;
        if (!immediate) func.apply(context, args);
      };
      var callNow = immediate && !timeout;
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
      if (callNow) func.apply(context, args);
    };
  };

  const animateMenuIcon = () => {
    selectors.menuIcon.addEventListener('click', () => {
      selectors.mobileNav.classList.toggle('mobile-nav-open');
      selectors.body.classList.toggle('noscroll');
      selectors.menuIcon.classList.toggle('open');
    });
  }
  const searchFormAnimation = () => {
    selectors.searchIcon.addEventListener('click', () => {
      selectors.searchIcon.style.display = "none";
      selectors.searchForm.classList.add('show')
    });
  }
  const mobileMenuInit = debounce(function(){
    const maxWidth = 992
    const menuContents = selectors.headerNav.innerHTML;
    if(window.innerWidth < maxWidth){
      selectors.mobileMenu.innerHTML = menuContents;
    }
  }, 100);

  const counter = () => {
    const counters = document.querySelectorAll('.counters-number');

      for(let n of counters) {
        const updateCount = () => {
          const target = + n.getAttribute('data-target');
          const count = + n.innerText;
          const speed = 2000;
          const inc = target / speed; 
          if(count < target) {
            n.innerText = Math.ceil(count + inc);
            setTimeout(updateCount, 1);
          } else {
            n.innerText = target;
          }
        }
        updateCount();
      }
  }

  const sliders = () => {
    if (selectors.postSlider) {
      new Glide('.post-slider').mount()
    }
  }

  const showMoreAnswers = () => {
    if (selectors.commentResponse && selectors.showMoreAnswersBtn){

      const [, ...rest] = selectors.commentResponse;
      rest.forEach(item => {
        item.classList.add('hide-answers')
      })
      
      selectors.showMoreAnswersBtn.addEventListener('click', () => {
        rest.forEach(item => {
          item.classList.toggle('hide-answers');
        })
        selectors.showMoreAnswersBtnText.classList.toggle('hide-answers');
        selectors.hideMoreAnswersBtnText.classList.toggle('hide-answers');
      })
      
    }
  }

  const showForm = () => {
    if(selectors.writeResponseBtn) {
      selectors.writeResponseBtn.addEventListener('click', () => {
        selectors.responseFormWrapper.classList.toggle('d-none');
      });
    }
  }

  const elementCounter = (item, el) => {
    if (item && el) {
      let items = item.length;
      el.innerText = items;
    }
  }

  const menuFilter = (category, link) => {
    let items = document.querySelectorAll('.filter-item[data-filter="' + category + '"]');
    const amountActiveItems = items.length;
    console.log(amountActiveItems);
    console.log(link);
    
    selectors.filterMenuItem.forEach(item => {
      item.classList.remove('active');
    })
    link.parentNode.classList.add('active');

    if(category == 'all'){
      console.log(selectors.filterItem)
      selectors.filterItem.forEach(item => {
        item.classList.remove('d-none')
      })
      selectors.emptyFilter.classList.add('d-none');

      return;
    }
    

    selectors.filterItem.forEach(item => {
      item.classList.add('d-none')
    })
    selectors.emptyFilter.classList.add('d-none');
    items.forEach(item => {
      item.classList.remove('d-none')
    })

    if(amountActiveItems === 0){
      selectors.emptyFilter.classList.remove('d-none');
      selectors.emptyFilter.classList.add('d-flex');
    }
  }
  const filterInit = () => {
    selectors.filterMenuLink.forEach(item => {
      item.addEventListener("click", () => {
        menuFilter(item.dataset.filter, item)
      });
    })
  }

  return {
    init: function() {
      mobileMenuInit();
      window.addEventListener("resize", function(){
        mobileMenuInit();
      });
      animateMenuIcon();
      searchFormAnimation();
      filterInit();
      counter();
      sliders();
      showForm();
      showMoreAnswers();
      elementCounter(selectors.portfolioItems, selectors.portfolioAmountItems);
      elementCounter(selectors.shopItems, selectors.shopAmoutItems);
    },
  }
}();

document.addEventListener('DOMContentLoaded', docReady, false);

function docReady () {
  dBlogApp.init();
  reframe(document.querySelectorAll('.vimeo-movie'))
}









