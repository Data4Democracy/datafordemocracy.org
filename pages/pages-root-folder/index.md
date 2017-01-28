---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
  image_fullwidth: header_unsplash_12.jpg
widget1:
  title: "Data for Democracy" 
  url: '/info/'
  image: widget-1-302x182.jpg
  text: 'Data people have a lot to offer. We’re driven by a passion to find the truth. We understand how information can be used to make better decisions and improve our communities. (Image - ?)'
widget2:
  title: "Active Projects"
  url: '/projects/'
  text: 'Write some words about how many ongoing projects we have, maybe highlighting something new and/or exciting.  Make the image something interesting from a project.'
  image: widget-1-302x182.jpg
widget3:
  title: "Partners"
  url: '/partners/'
  image: widget-github-303x182.jpg
  text: 'Make the image a collage of their logos.  Write some words about how awesome people like supporting our work and working with us.'
#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
callforaction:
  url: /join_us/
  text: Join Us ›
  style: alert
permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---

