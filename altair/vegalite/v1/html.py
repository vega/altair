HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <script src="https://cdn.jsdelivr.net/npm/vega@2"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@1"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@2"></script>
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
