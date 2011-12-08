Django Admin Honeypot Signals
===============================

If you are using the admin_honeypot App to log failed login attempts, you may want to be notified via email. 

**Features:**

If someone tries to login using the wrong admin url, django-admin-honeypot creates a new model instance, which includes all significant information about this attempt. After save() the signal handler sends a notification email to settings.MANAGERS, which includes the basic model information.


How to use
==========

Get und implement django-admin-honeypot:

* `django-admin-honeypot <https://github.com/dmpayton/django-admin-honeypot>`_

Make sure it is working perfect.

* Install this package::

    pip install -e git://github.com/bitmazk/django-honeypot-signals#egg=honeypot_signals

* Add ``honeypot_signals`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        [...]
        'honeypot_signals',
    }

* Add ``MANAGERS`` to your ``settings.py``::

    MANAGERS = (
        ('Foo Bar', 'foobar@example.com'),
    )

