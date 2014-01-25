cms-api-client
==============

A desktop client written in Python that allows you to manage your contents,
categories, etc.

Interaction with server
=======================

The API will be provided by the WCF extensions and by the respective
applications based upon it. This client is specifically intended for the
to be made CMS.

Contents
========

The meta data of the contents is saved in a database on the server.
But the actual content of the contents is saved in files. The client
therefore manages a Git repository that contains these actual contents
offline. Whenever you sync the client with the server, local changes are
pushed to the server and vice versa.

Motivation
==========

By having the actual contents in files it is possible for you to 
edit them with whatever editor you see fit and then sync them with this
client. As the client uses public facing API you can alternatively write
your own client(s) or just upload the files to the respective directory.

This allows for automatic deployment of new articles and collaborative
editing.
