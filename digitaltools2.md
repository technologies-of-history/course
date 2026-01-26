---
layout: page
title: Digital Tools Assignment 2
permalink: /digitaltools2
---
# Showing History

Now that you've mastered the work flow of creating a new branch in our repository, creating a Markdown file, writing a post in Markdown syntax, committing your changes, and creating a pull request, you're ready to begin to create digital historical scholarship incorporating other digital tools. In this assignment, you'll practice dropping snippets of code bracketed by `<html>` tags into your post so that readers can interact with the product of your digital scholarship right on your site. You'll continue to employ this basic tactic of embedding other digital tools into our static site in later digital tools assignments.

In this assignment, you'll be asked to compose a 3-4 paragraph post reflecting on the ubiquity of epigraphic writing in ancient Rome, paying special attention to a single inscription that you'll select from the [Epigraphic Database Heidelberg](https://edh.ub.uni-heidelberg.de/), and incorporating a map showing sites of surviving Roman epigraphy in a single Roman province. In your post, you'll include a map of surviving Roman inscriptions in a single Roman province created with [Leaflet](https://leafletjs.com), an open-source JavaScript library for creating interactive maps on the web. You'll also include an image of your chosen inscription viewed in [Mirador](https://projectmirador.org), an open-access IIIF viewer.


## Step 1: Visit the Heidelberg Epigraphic Database

1. Browse the selection of ancient Roman epigraphy that appears when you choose a single Roman province from the drop-down menu in the [photographic database](https://edh.ub.uni-heidelberg.de/foto/suche) search page. After perusing the selection from different provinces, choose one province to work with. For the purposes of this exercise, you should choose a province with no more than 350 or so results.
2. Run a search for inscriptions from your chosen province, and click the option at the bottom to **sort by** and select **HD no.** 
3. Once you've selected your province and generated the search results, you'll see a link at the top of the page (above the list of results) with a link to download the results as a **.csv file.** Click the link to download the file, then save it on your computer.
4. Next, select one inscription from the results that appear for your chosen Roman province, making sure that the inscription you pick has good quality images and an **HD number** link. Click the **HD number** link and keep the page open on your browser. You'll need it in a few steps.

## Step 2: Add Geo Coordinates into your .CSV

1. Open the **.csv file** that you downloaded from the Heidelberg Epigraphy Database and sort the data according to **ancient find spot** so that the same places are grouped together. 
2. Create a new spreadsheet on your computer that just contains the location information for the inscriptions compiled in the **.csv file** you've downloaded from the EDH.
3. Next, visit [Pleiades](https://pleiades.stoa.org/places/) and search for each of your ancient placenames. Since lots of inscriptions come from the same place, you won't need to do this for each inscription, just each place name.
4. Copy-and-paste the latitude and longitude coordinates from Pleiades into your **.csv file** in a new column next to each ancient place name.

## Step 3: Create your map with LeafletJS

1. Create a new Markdown file for your post following our course protocols (open or fork the **spring-2026** repository in your **personal** GitHub account, navigate to **_posts** and create a new .md file titled **yyyy-mm-dd-your title.md** with the appropriate YAML header.)
2. To embed a Leaflet map into your post, you'll copy the snippet of code below into your Markdown file. Always be sure to wrap snippets of code in `<html>` tags. Below, you'll find the code you need for your map. The first few lines of code tell the browser to import Leaflet's CSS style sheet and JavaScript code from the web. These lines are all written in HTML. Below those first few lines of HTML, the `<script>` tag tells your browser that what follows is JavaScript, which you'll customize to render the Leaflet map.

```
<html>
<div style="margin: 2rem 0;">
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>

  <div id="map" style="position: relative; height: 500px; width: 100%;"></div>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
    <script>
    const map = L.map('map').setView([46.60, 1.51], 6);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
var marker = L.marker([46.59, 1.52]).addTo(map).bindPopup('Argentomagus').openPopup();
</script>
</div>
</html>
```

**Once you've got this code in your Markdown post, you'll change the following bits:**

`var map = L.map('map').setView([46.60, 1.51], 6);`  
You'll need to update the `set.View` to the latitude and longitude coordinates that you want to be the center of your map, and designate how zoomed in you want the map to be on loading. In the example here, those coordinates are `[46.60, 1.51]`, and the zoom is set to `6`. Update those coordinates with what you'd like to be the center of your map, and set the zoom (a higher number zooms in more and a lower number zooms out).

Ignore the next few lines, as these lines import the base map layer from [OpenStreetMap](https://www.openstreetmap.org/#map=9/47.082/2.398), which provides open-access digital maps.

`var marker = L.marker([46.59, 1.52]).addTo(map).bindPopup('Argentomagus').openPopup();`  
This line of code indicates where to put a marker on your map and what to label it with a pop-up when the marker is clicked. Again, you need to update the lat/long coordinates, `[46.59, 1.52]` in this example, to the location of each of the inscription locations in your Roman province. You'll also change `('Argentomagus')` to the ancient placename of that site.

You'll repeat this line of code (with updated lat/long and placename) for every marker you want to display on your map.

**If all goes well, you'll have a map that looks something like this, but centered on your chosen Roman province:**

<html>
<div style="margin: 2rem 0;">
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>

  <div id="map" style="position: relative; height: 500px; width: 100%;"></div>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
    <script>
  const map = L.map('map').setView([46.60, 1.51], 6);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);
  var marker = L.marker([46.59, 1.52]).addTo(map).bindPopup('Argentomagus').openPopup();
  var marker = L.marker([47.08, 2.40]).addTo(map).bindPopup('Avaricum').openPopup();
  var marker = L.marker([44.84, -0.58]).addTo(map).bindPopup('Burdigalia').openPopup();
  var marker = L.marker([46.59, 0.35]).addTo(map).bindPopup('Limonum Pictonum').openPopup();
  var marker = L.marker([45.74, -0.63]).addTo(map).bindPopup('Mediolanum Sanctonum').openPopup();
  var marker = L.marker([43.66, 0.52]).addTo(map).bindPopup('Ausci').openPopup();
  var marker = L.marker([45.54, -0.88]).addTo(map).bindPopup('Tamnum').openPopup();
  var marker = L.marker([43.03, 0.57]).addTo(map).bindPopup('Lugdunum Convenarum').openPopup();
</script>
</div>
</html>

## Step 4: Add an image of your inscription with a IIIF viewer

1. You could obviously use Markdown to include an image in your post, as long as that image has a URL. But we know that IIIF viewers like [Mirador](https://projectmirador.org) enable the display of high-res images, with interactive, zoom capabilities. Mirador also makes the image metadata easily viewable, and allows for the display of multiple images, side-by-side--though we'll just display one here.
2. First, click the link to open the **IIIF manifest** for your chosen inscription. You'll find a link to the IIIF manifest for each inscription in the page you opened by clicking the **HD number** for your inscription.
2. Next, you'll add the following snippet of code into your Markdown post, again with the `<html>` tags wrapping the code. Again, the first few lines of code tell the browser to load information from the web: a font family from Google fonts, as well as the CSS stylesheet for Mirador, followed by the JavaScript code for Mirador functionality Below that, following `<script>`, is the JavaScript code to create the Mirador viewer in your post.

```
<html>
<div style="margin: 2rem 0;">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500">
  <link rel="stylesheet" href="https://unpkg.com/mirador@latest/dist/mirador.min.css">
  
  <div id="my-mirador" style="position: relative; height: 500px; width: 100%;"></div>
  
  <script src="https://unpkg.com/mirador@latest/dist/mirador.min.js"></script>
    <script>
      const mirador = Mirador.viewer({
        id: "my-mirador",
        manifests: {
          "URLforyourmanifest.json": { provider: "Epigraphic Database Heidelberg" }
        },
        windows: [
          { loadedManifest: "URLforyourmanifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' }
        ]
      })();
</script>
</div>
</html>
```
**Once you've got the code in your Markdown post, you'll need to update the following bits:**

`manifests: { "URLforyourmanifest.json": { provider: "Epigraphic Database Heidelberg" }`  
Where you see "URLforyourmanifest.json" copy-and-paste the URL for the IIIF manifest of your chosen inscription. Be sure to keep the quotation marks!

`{ loadedManifest: "URLforyourmanifest.json",`  
Where you see "URLforyourmanifest.json" again, copy-and-paste the URL for the IIIF manifest of your chosen inscription. Be sure to keep the quotation marks!


**If you've done it correctly, your post will include a viewer that looks like this, with your image and metadata from EDH visible.**

<html>
<div style="margin: 2rem 0;">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500">
  <link rel="stylesheet" href="https://unpkg.com/mirador@latest/dist/mirador.min.css">
  
  <div id="my-mirador" style="position: relative; height: 500px; width: 100%;"></div>
  
  <script src="https://unpkg.com/mirador@latest/dist/mirador.min.js"></script>
    <script>
      const mirador = Mirador.viewer({
        id: "my-mirador",
        manifests: {
          "https://technologies-of-history.github.io/course/assets/iiif/manifest3.json": { provider: "Epigraphic Database Heidelberg" }
        },
        windows: [
          { loadedManifest: "https://technologies-of-history.github.io/course/assets/iiif/manifest3.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' }
        ]
      })();
</script>
</div>
</html>


## Step 5: Compose your post

Before, after, or in between your map and image viewer, compose 3-4 paragraphs in Markdown responding to the following prompts:
- Describe your chosen inscription, including what we know about what it says, when it was written, where, and by whom. 
- What does your map of surviving inscriptions reveal about Roman attitudes toward public writing? 
- Finally, how do you think digital tools like high-res imaging and digital mapping change how the public understands the role of writing in Roman society?

## Step 6: Initiate a pull request to submit your post

1. Once you've **Committed changes...** to your repository, you'll need to initiate a pull request to the **technologies-of-history/spring-2026** repository. Don't do so until you're sure you've got your post exactly as you want it!
2. When you do initiate a pull request, be sure that your repository is the **head** and the **base** is **technologies-of-history/spring-2026**.
4. Name your pull request **LastName_dt2** and then click **Create pull request**.

Ok, that's it! You're done!
