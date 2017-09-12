EmailRelay
==========

Forward all incoming e-mail according to alias file.

![Build status](https://travis-ci.org/jylitalo/EmailRelay.svg?branch=master) 

Requirements
------------

Host that is willing to accept e-mail from us (for example SendGrid or Mailgun).

Apt-based Linux distribution with Postfix.

Role Variables
--------------

* relayhost: smtp.mailgun.org
* relayport: 2525
* smtp_user: invalid
* smtp_password: invalid
* aliases:
  * {alias: invalid, destination: invalid@foobar.invalid}

Dependencies
------------

None

Example Playbook
----------------

    - hosts: server
      roles:
         - { role: EmailRelay, smtp_user: foobar }

License
-------

MIT

Author Information
------------------

Juha Ylitalo, juha.ylitalo@gmail.com, http://www.ylitalot.com/
