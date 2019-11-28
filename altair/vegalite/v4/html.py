HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <script src="https://cdn.jsdelivr.net/npm/vega@5></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@4"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
</head>
<body>
  <div id="vis"></div>
  <script type="text/javascript">
    var spec = {spec};
    var opt = {opt};
    vegaEmbed("#vis", spec, opt);
  </script>
</body>
</html>
"""
