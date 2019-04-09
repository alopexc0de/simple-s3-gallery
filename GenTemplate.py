#!/usr/bin/env python3
# GenThumb.py - Part of the simple s3 gallery
# Usage: ./GenThumb.py

from pathlib import Path

baseuri = "https://s3.wasabisys.com/c0de-photography/"
thumb_path = "./thumbs"
pathlist_file = "pathlist_EOS 30D:10.03.2015 - Jay Cooke:.txt" # Index file created by GenThumb.py

template = """
<html>
    <head>
        <title>Simple S3 Gallery</title>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="David Todd" />
        <link rel="icon" type="image/png" href="https://secure.gravatar.com/avatar/1e346a54257cf0a9932fcfc1e61c015d" />

        <!-- Bootstrap core CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <style>
            .jumbotron {
                padding-top: 3rem;
                padding-bottom: 3rem;
                margin-bottom: 0;
                background-color: #fff;
            }
            @media (min-width: 768px) {
                .jumbotron {
                    padding-top: 6rem;
                    padding-bottom: 6rem;
                }
            }

            .jumbotron p:last-child {
                margin-bottom: 0;
            }

            .jumbotron-heading {
                font-weight: 300;
            }

            .jumbotron .container {
                max-width: 40rem;
            }

            footer {
                padding-top: 3rem;
                padding-bottom: 3rem;
            }

            footer p {
                margin-bottom: .25rem;
            }
        </style>
    </head>
    <body>
        <header>
            <div class="collapse bg-dark" id="navbarHeader">
                <div class="container">
                    <div class="row">
                        <div class="col-sm-8 col-md-7 py-4">
                            <h4 class="text-white">About</h4>
                            <p class="text-muted">This was a small gallery that I put together to make my photography available to the world. Images are grouped in folders for what I've done.</p>
                        </div>
                        <div class="col-sm-4 offset-md-1 py-4">
                            <h4 class="text-white">Contact</h4>
                            <ul class="list-unstyled">
                                <li><a href="https://c0defox.es" class="text-white">My contact site</a></li>
                                <li><a href="https://t.me/c0defox" class="text-white">Hit me up on Telegram</a></li>
                                <li><a href="c0de#0689" class="text-white">My Discord is c0de#0689</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="navbar navbar-dark bg-dark shadow-sm">
                <div class="container d-flex justify-content-between">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="mr-2" viewBox="0 0 24 24" focusable="false"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
                    <strong>Simple S3 Gallery</strong>
                </a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarHeader" aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                </div>
            </div>
        </header>

        <main role="main">

            <!-- Optional for creating a notification -->
            <!--
            <section class="jumbotron text-center">
                <div class="container">
                    <h1 class="jumbotron-heading">Album example</h1>
                    <p class="lead text-muted">Something short and leading about the collection below—its contents, the creator, etc. Make it short and sweet, but not too short so folks don’t simply skip over it entirely.</p>
                    <p>
                        <a href="#" class="btn btn-primary my-2">Main call to action</a>
                        <a href="#" class="btn btn-secondary my-2">Secondary action</a>
                    </p>
                </div>
            </section>
            -->

            <div class="album py-5 bg-dark">
                <div class="container">
                    <div class="row">
                        {{THUMBROW}}
                    </div>
                </div>
            </div>
        </main>

        <footer class="text-muted">
            <div class="container">
                <p class="float-right"><a href="#">Back to top</a></p>
                <p>Simple S3 Gallery &copy; 2019 <a href="https://c0defox.es">David Todd</a> - All photos are &copy; <a href="https://dtodd.us">David Todd</a></p>
            </div>
        </footer>

        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
</html>
"""

template2 = """
<div class="col-md-4">
    <a href="{{FULLLINK}}" target="{{FULLLINK}}">
        <div class="card mb-4 bg-dark text-white">
            <div class="card-header">{{TITLE}}</div>
            <img class=card-img" width="100%" height="100%" src="{{THUMBNAIL}}" />
        </div>
    </a>
</div>
"""

thumblist = list(Path(thumb_path).rglob("*.[jJ][pP][gG]"))

with open(pathlist_file, 'r') as pathlist:
    with open('index_%s.html' % pathlist_file.strip("pathlist_").strip(".txt"), 'w') as index:
        pathlist = "%s" % pathlist.read()
        pathlist = pathlist.splitlines()
        thumbrow = ""
        for image in thumblist:
            indices = [i for i, s in enumerate(pathlist) if image.name in s]
            if len(indices) > 0:
                imagename = "%s" % image
                the_template = template2
                the_template = the_template.replace("{{FULLLINK}}", pathlist[indices[0]])
                the_template = the_template.replace("{{TITLE}}", imagename.strip("thumbs/"))
                thumbrow += the_template.replace("{{THUMBNAIL}}", "%s" % image)
        index.write(template.replace("{{THUMBROW}}", thumbrow))

