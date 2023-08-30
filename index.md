---
layout: default
title: Student Blog
---

## Hayden's Page

Subscribe to my [Youtube channel](https://youtube.com/@84115) !!
Go to my [Github account](https://github.com/monke7769)

## About me
DNHS student, class of '26. Loves CS and math. 3 years of python experience, 3 years of bash experience, 2 months of C++

### Achievements

- 1918 AoPS FTW rating (global #11)
- USACO Silver
- USAJMO qualifier
- 140 top wpm
- 17k brawl stars trophies
- 5 on AP Music Theory 🤣
- crossy road top score 1000
- 3 years of Python experience, C++ novice

Freeform 
-------------

![](https://i.ibb.co/yRk7Lk2/Screenshot-2023-08-22-at-7-43-54-PM.png) 

###### am also future piktur arteest

## Mon 8/21

Finished setting up student repo. Started with a bit of blogging. 
### Plans

Figure out how the make command works? I'm currently using 
```
bundle exec jekyll serve 
```
to host the site locally - which is putting the site at [127.0.0.1:4000/student/](127.0.0.1:4000/student/). Hopefully I figure this out soon
```
make: *** [_posts/2023-08-17-AP-pseudo-vs-python_IPYNB_2_.md] Error 1
```

### Tools

The biggest tool involved in the making of this website is Makefile. Makefile defines a set of tasks to be executed, such as in the case of having a website, it will define tasks such as starting the local server, starting logging, and converting notebook files to Markdown to be read.

## Tues 8/22

Figured out make (finally) the command that fixed everything was 
```
ln -s /opt/homebrew/share/jupyter/nbconvert ~/Library/Jupyter
```
hopefully no more problems with setting up the site. working on putting images and new theme on the about me page.

![](https://i.ibb.co/1J2pjBV/Screenshot-2023-08-23-at-10-21-51-AM.png)

## Thurs 8/24

I want to use this theme:
[https://github.com/abhinavs/moonwalk](https://github.com/abhinavs/moonwalk)

It looks so good but I haven't figured out how to import the theme into my github pages
I have changed the _config.yml file to use 
```
remote_theme: abhinavs/moonwalk
```
and even tried copy-pasting the contents of moonwalk.gemspec into this repo's Gemfile but neither has worked.. 
right now running the server gives me a file not found error
![](https://images2.imgbox.com/49/37/6VbkoAzQ_o.png)
I'm going to try to investigate the cause of the error in _includes/head.html and in _layouts. wish me luck

## Fri 8/25

Learned/reviewed some of the basics in Python. From now on, blogging with code will be in the "Blog" section of the site (using *.ipynb files) and located in the table in the CompSci Notebook page.

<style>

  body {
      background-color: #874e28;
      color: #FF5B09;
      animation: fadeInAnimation ease 3s;
      animation-iteration-count: 1;
      animation-fill-mode: forwards;
  }
  @keyframes fadeInAnimation {
      0% {
          opacity: 0;
      }
      100% {
          opacity: 0.75;
      }
  }

  h1::before {
  transform: scaleX(0);
  transform-origin: bottom right;
}

h1:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}

h1::before {
  content: " ";
  display: block;
  position: absolute;
  top: 0; right: 0; bottom: 0; left: 0;
  inset: 0 0 0 0;
  background: rgb(37, 73, 28);
  z-index: -1;
  transition: transform .3s ease;
}

h1 {
  position: relative;
  color: #e454eb;
  font-size: 3rem;
  font-family: Monospace;
}
p {
  font-family: Monospace;
}

html {
  block-size: 100%;
  inline-size: 100%;
}

body {
  min-block-size: 100%;
  min-inline-size: 100%;
  margin: 0;
  box-sizing: border-box;
  display: grid;
  place-content: center;
  font-family: system-ui, sans-serif;
  color: #99E8C3;
}

h2 {
  position: relative;
  color: #FD4F04;
  font-size: 2rem;
  font-family: Monospace;
}

h3 {
  position: relative;
  color: #0BEDF5;
  font-size: 1rem;
  font-family: Monospace;
}
.block-container {
    padding-top: 1rem;
    padding-bottom: 0rem;
    padding-left: 5rem;
    padding-right: 5rem;
}

@media (orientation: landscape) {
  body {
    grid-auto-flow: column;
  }
}
</style>