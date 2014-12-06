=====
Mailsender
=====

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "mailsender" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'app_mailsender',
      )

2. Include the polls URLconf in your project urls.py like this::

      url(r'^mailsender/', include('polls.urls')),

3. Run `python manage.py syncdb` to create the polls models.


4. Visit http://127.0.0.1:8000/ to participate in the poll.