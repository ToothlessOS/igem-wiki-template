# Libraries used:

## Frontend

1. bootstrap 5.3.3

## Backend

1. jQuery 3.7.1

## Visualization & Bio specific

1. 3dmol (for molecule visualization)
2. d3.js 7.9.0 (powerful visualization tool; Note: for our purpose, use 'UMD+Local' setup; Ref: [Getting started | D3 by Observable](https://d3js.org/getting-started#d3-in-vanilla-html))
3. cytoscape.js 3.31.2 (for visualizing enzyme reaction network)
4. chart.js 4.4.1 (Interactive chart visualization)
5. escher 1.8.1 (Visualizing metabolic pathways)

## Imports (example)

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}{% endblock %} -ToothlessOS</title>

    <!-- Customized Bootstrap Stylesheet -->
    <!--Fixed the routing problem with url_for() in flask-->
    <!-- Bootstrap -->
    <link href="{{ url_for('static', filename='css/bootstrap.min.css') }}" rel="stylesheet">
  </head>
  <body>
     <!-- JavaScript Libraries -->
     <!-- JQuery -->
     <script src="{{ url_for('static', filename='js/jquery-3.7.1.min.js') }}"></script>
     <!-- Bootstrap -->
     <script src="{{ url_for('static', filename='js/bootstrap.bundle.min.js') }}"></script>
     <!--3dmol-->
     <script src="{{ url_for('static', filename='js/3Dmol-min.js') }}"></script>
     <!--d3.js-->
     <script src="{{ url_for('static', filename='js/d3.v7.min.js') }}"></script>
     <!--cytoscape.js-->
     <script src="{{ url_for('static', filename='js/cytoscape.min.js') }}"></script>
     <!--chart.js-->
     <script src="{{ url_for('static', filename='js/chart.umd.min.js') }}"></script>
     <!--escher-->
     <script src="{{ url_for('static', filename='js/escher.min.js') }}"></script>

    <!-- Navigation -->
    {% include 'menu.html' %}

    <!-- Page Content -->
    {% block page_content %}{% endblock %}

    <!-- Footer -->
    {% include 'footer.html' %}

  </body>
</html>
```
