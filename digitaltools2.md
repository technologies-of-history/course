---
layout: page
title: Digital Tools Assignment 2
permalink: /digitaltools2
---
# Showing History

Now that you've mastered the work flow of creating a new branch in our repository, creating a Markdown file, writing a post in Markdown syntax, committing your changes, and creating a pull request, you're ready to begin to create digital historical scholarship incorporating other digital tools. In this assignment, you'll practice dropping snippets of JavScript code bracketed by `<html>` tags into your post so that readers can interact with the product of your digital scholarship right on your site. You'll continue to employ this basic tactic of embedding other digital tools into our static site in later digital tools assignments.

In this assignment, you'll be asked to compose a 3-4 paragraph post reflecting on the ubiquity of epigraphic writing in ancient Rome, paying special attention to a single inscription that you'll select from the [Epigraphic Database Heidelberg](https://edh.ub.uni-heidelberg.de/). In your post, you'll include a map of surviving Roman inscriptions in a single Roman province created with [Leaflet](https://leafletjs.com), an open-source JavaScript library for creating interactive maps on the web. You'll also include an image of your chosen inscription displayed in [Mirador](https://projectmirador.org), an open-access IIIF viewer, also written in JavaScript. The Mirador viewer is able to read a remote JSON (JavaScript Object Notation) file containing both image data and metadata for the inscription in question, rendering both in the viewer window in such a way that users can interact with the image.

There are a lot of steps here, I know, but we'll work together on Steps 1 and 2 in class on Thursday, February 5 and Steps 3 and 4 in class on Thursday, February 12. This assignment is due on GitHub by 11:59 pm on Friday, February 20.

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

1. In the previous assignment, you forked our **spring-2026** repository into your **personal** GitHub account to write your assignment and then generate a pull request. For this assignment, you're going to work directly within the **technologies-of-history/spring-2026** repository so that you can try out GitHub's CodeSpaces to check your work.
2. In our **technologies-of-history/spring-2026** repository, create a new branch called **lastname-dt2**. In that branch, navigate to the **_posts** folder and create a new .md file titled **yyyy-mm-dd-your title.md** with the appropriate YAML header. *Note: Do not name your file Digital Tools 2. We can't have multiple files merged with the same filename. They'll overwrite one another once I merge your post into the course repo. Think of something more creative!*
3. To embed a Leaflet map into your post, you'll copy the snippet of code below into your Markdown file. Always be sure to wrap snippets of code in `<html>` tags. 


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
*The first few lines of this code tell the browser to import Leaflet's CSS style sheet and JavaScript code from the web. These lines are all written in HTML. Below those first few lines of HTML, the `<script>` tag tells your browser that what follows is JavaScript, which you'll customize to render the Leaflet map.*

**Once you've got this code in your Markdown post, you'll change the following bits:**

`var map = L.map('map').setView([46.60, 1.51], 6);`  
You'll need to update the `set.View` to the latitude and longitude coordinates that you want to be the center of your map, and designate how zoomed in you want the map to be on loading. In the example here, those coordinates are `[46.60, 1.51]`, and the zoom is set to `6`. Update those coordinates with what you'd like to be the center of your map, and set the zoom (a higher number zooms in more and a lower number zooms out).

Ignore the next few lines, as these lines import the base map layer from [OpenStreetMap](https://www.openstreetmap.org/#map=9/47.082/2.398), which provides open-access digital maps.

`var marker = L.marker([46.59, 1.52]).addTo(map).bindPopup('Argentomagus').openPopup();`  
This line of code indicates where to put a marker on your map and what to label it with a pop-up when the marker is clicked. Again, you need to update the lat/long coordinates, `[46.59, 1.52]` in this example, to the location of each of the inscription locations in your Roman province. You'll also change `('Argentomagus')` to the ancient placename of that site.

You'll repeat this line of code (with updated lat/long and placename) for every marker you want to display on your map.

**Commit your changes and move to the next step!**

## Step 4: Add an image of your inscription with a IIIF viewer

1. You could obviously use Markdown to include an image in your post, as long as that image has a URL. But we know that IIIF viewers like [Mirador](https://projectmirador.org) enable the display of high-res images, with interactive, zoom capabilities. Mirador also makes the image metadata easily viewable, and allows for the display of multiple images, side-by-side--though we'll just display one here.
2. First, click the link to open the **IIIF manifest** for your chosen inscription. You'll find a link to the IIIF manifest for each inscription in the page you opened by clicking the **HD number** for your inscription.
2. Next, you'll add the following snippet of code into your Markdown post, again with the `<html>` tags wrapping the code. 


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
*Again, the first few lines of this code tell the browser to load information from the web: a font family from Google fonts, as well as the CSS stylesheet for Mirador, followed by the JavaScript code for Mirador functionality. Below that, following* `<script>`*, is the JavaScript code to create the Mirador viewer in your post.*

**Once you've got the code in your Markdown post, you'll need to update the following bits:**

`manifests: { "URLforyourmanifest.json": { provider: "Epigraphic Database Heidelberg" }`  
Where you see "URLforyourmanifest.json" copy-and-paste the URL for the IIIF manifest of your chosen inscription. Be sure to keep the quotation marks!

`{ loadedManifest: "URLforyourmanifest.json",`  
Where you see "URLforyourmanifest.json" again, copy-and-paste the URL for the IIIF manifest of your chosen inscription. Be sure to keep the quotation marks! 

**Commit your changes and move to the next step!**

## Step 5: Compose your post

Before, after, or in between your map and image viewer, compose 3-4 paragraphs in Markdown responding to the following prompts:
- Describe your chosen inscription, including what we know about its location and its date. Can you make out any of the letters? 
- What might your map of surviving inscriptions tell us about the way Roman people practiced the "epigraphic habit"? Do you find inscriptions in towns, villas, or on monuments? (You may want to look again at [Pleiades](https://pleiades.stoa.org/places/) to see what sort of ancient sites you're working with.)
- Finally, referring to MacMullen's article on the "epigraphic habit" in Rome, do you think digital tools like high-res imaging and digital mapping change how historians might interpret the rise and fall of the "epigraphic habit" in Roman society?

**Commit your changes and move to the next step!**

## Step 6: Check that your post looks the way it should

The beauty of working directly in our GitHub organization repository is that you can use GitHub CodeSpaces to check your JavaScript before you submit your pull request. This is particularly helpful when you're importing bits of code that aren't Markdown into your post, because the default GitHub preview won't read those bits and render them the way a web browswer will. What you want are maps and Mirador viewers that look something like this:

**LeafletJS Map of Roman Aquitania**
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

**Mirador IIIF viewer with manifest from EDH**
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
          "https://technologies-of-history.github.io/spring-2026-data/iiif/manifest3.json": { provider: "Epigraphic Database Heidelberg" }
        },
        windows: [
          { loadedManifest: "https://technologies-of-history.github.io/spring-2026-data/iiif/manifest3.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' }
        ]
      })();
</script>
</div>
</html>

If your map doesn't look the way you want it to, or your IIIF isn't loading, you can make changes to your code and check the fixes in real time. To do this, you need to create a Codespace in the branch you've named **lastname-dt2** of our class repository. Click [here]( {{ site.baseurl }}/codespaces) for instructions on how to serve your blog post virtually using GitHub CodeSpaces.


## Step 7: Initiate a pull request to submit your post

1. Once you've **Committed changes...** in your **lastname-dt2** branch, you'll need to initiate a pull request to the **master** branch of the **technologies-of-history/spring-2026** repository. Don't do so until you're sure you've got your post exactly as you want it!
2. When you do initiate a pull request, be sure that your branch is the **head** and the **master** branch is **base**.
3. Name your pull request **Digital Tools 2** and then click **Create pull request**.

Ok, that's it! You're done!
