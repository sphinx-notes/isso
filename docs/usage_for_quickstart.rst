.. note:: Before using the extension, you should have an Isso__ instance deployed.

Still in conf.py, set ``isso_url`` :doc:`conf` item to the URL of your Isso instance.

.. code-block:: py

   isso_url = 'https://HOST:PORT'

Then use directive ``isso`` to embed Isso comment box to your doccument:

.. code-block:: rst

   .. isso::

Just like this:

.. isso::

Feel free to comment~

__ https://isso-comments.de/
