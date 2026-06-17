=============
Configuration
=============

.. autoconfval:: isso_url

   HTTP URL points to your Isso server.


.. autoconfval:: isso_client_config

   A mapping that corresponding to `Isso Client Configuration`_.

   .. versionadded:: 2.0

   .. _Isso Client Configuration: https://posativ.org/isso/docs/configuration/client/


.. autoconfval:: isso_exclude_patterns

   A list of `glob-style patterns`_ that should be excluded when inserting Isso
   comment thread.
   They are matched against the document name (docname).
   :confval:`isso_exclude_patterns` has priority over :confval:`isso_include_patterns`.

   .. versionadded:: 2.0

   .. _glob-style patterns: https://www.sphinx-doc.org/en/master/usage/configuration.html#glob-style-patterns


.. autoconfval:: isso_include_patterns

   A list of `glob-style patterns`_ that are used to insert Isso comment thread.
   They are matched against the document name (docname).
   :confval:`isso_exclude_patterns` has priority over :confval:`isso_include_patterns`.

   .. versionadded:: 2.0
