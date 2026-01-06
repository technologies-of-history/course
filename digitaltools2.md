---
layout: page
title: Digital Tools Assignment 2
permalink: /digitaltools2
---
## Showing History

Now that you've mastered the work flow of creating a new branch in our repository, creating a Markdown file, writing a post in Markdown syntax, committing your changes, and creating a pull request, you're ready to begin to create digital historical scholarship incorporating other digital tools. In this assignment, you'll practice embedding `<html>` code so that readers can interact with the product of your digital scholarship right on your site. You'll continue to employ this basic tactic of embedding other digital tools into our static site in later digital tools assignments.

### Step 1: Visit the Heidelberg Epigraphic Database

1. Browse the selection of ancient Roman epigraphy that appears when you choose a single Roman province from the drop-down menu in the [photographic database](https://edh.ub.uni-heidelberg.de/foto/suche) search page. After perusing the selection from different provinces, choose one province to work with. For the purposes of this exercise, you should choose a province with no more than 350 or so results.
2. Run a search for inscriptions from your chosen province, and click the option at the bottom to **sort by** and select **HD no.** 
3. Once you've selected your province and generated the search results, you'll see a link at the top of the page (above the list of results) with a link to download the results as a **.csv file.** Click the link to download the file, then save it on your computer.
4. Next, select four inscriptions from the results that appear for your chosen Roman province, making sure that the inscriptions you pick have good quality images and that the have an **HD number** link. I'd suggest picking a range of inscriptions that include both formal epigraphy and informal graffiti-style carving. For each of the inscriptions you've chosen, click the **HD number** link and keep the page open on your browser. You'll need it in a few steps.

### Step 2: Create your Google MyMaps
1. Open the **.csv file** that you downloaded from the Heidelberg Epigraphy Database and sort the data according to **modern find spot** so that the same places are grouped together. 
2. Create a new spreadsheet on your computer that just contains the location information for the inscriptions compiled in the **.csv file** you've downloaded from the EDH. You'll want to be sure to include both ancient and modern location information.
3. Next, navigate to [Google My Maps](https://mymaps.google.com). Log in if you haven't, and click **Create New Map.**
4. Name your map and then click **Import**. Drag and drop the new **.csv file** with just the location information for the inscriptions. Adjust the settings in Google MyMaps so that locations on your map are labeled with ancient placenames, but appear in the appropriate modern location.
6. Play around with the styling and background until the map looks the way you'd like.
7. Click **share** in the My Maps menu, and share the map via your Google drive. No need to email it to anyone. Once your map is public, you can click the three dots at the top right of the MyMaps menu and select **Embed on my site.**

### Step 3: Create your post

1. Create a new Markdown file for your post following our course protocols (create a new branch in **spring-2026** called **lastname-dt2**, navigate to **_posts** and create a new .md file titled **yyyy-mm-dd-your title.md** with the appropriate YAML header.) 
2. Compose a 3-4 paragraph post responding to the following prompt. Your blog post must also include the Google MyMaps you've created, as well as images of the four inscriptions you've chosen to analyze.

Referencing the transcriptions and images for your four inscriptions on the Heidelberg Epigraphic Database, Cooley and Bispham's chapter, and your map illustrating the geographic distribution of epigraphic writing in your chosen province, what do these pieces of evidence tell us about Roman attitudes toward public writing? In what ways might these digital reproductions of ancient epigraphy change our perception of the role of writing in the ancient world?

3. To embed, your Google MyMaps somewhere in the post, copy the code that appears when you click **Embed on my site** somewhere in your post, making sure that you wrap the code in `<html> </html>` tags. 
4. To embed a Mirador viewer into your blog post, you'll cut and pase the following code into your post somewhere. After you've pasted the code into your Markdown file, you'll copy-and-paste the URL for each of the IIIF manifests of your chosen inscriptions into the appropriate spot indicated in the code snippet below. You'll find a link to the IIIF manifest for each inscription in the page you opened by clicking the **HD number** link on the EDH website.

```
<html>
<div style="margin: 2rem 0;">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500">
  <link rel="stylesheet" href="https://unpkg.com/mirador@latest/dist/mirador.min.css">
  
  <div id="my-mirador" style="position: relative; height: 600px; width: 100%;"></div>
  
  <script src="https://unpkg.com/mirador@latest/dist/mirador.min.js"></script>
    <script type="text/javascript">
  (function() {
    if (typeof Mirador !== 'undefined') {
      var mirador = Mirador.viewer({
        id: "my-mirador",
        manifests: {
          "URL for the first image manifest here": { provider: "Epigraphic Database Heidelberg" },
          "URL for the second image manifest here": { provider: "Epigraphic Database Heidelberg" },
          "URL for the third image manifest here": { provider: "Epigraphic Database Heidelberg" },
          "URL for the fourth image manifest here": { provider: "Epigraphic Database Heidelberg" }
        },
        windows: [
          { loadedManifest: "URL for the first image manifest here", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "URL for the second image manifest here", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "URL for the third image manifest here", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "URL for the fourth image manifest here", canvasIndex: 0, thumbnailNavigationPosition: 'none' }
        ]
      });
    }
  })();
</script>
</div>
</html>
```


If you've done it correctly, your post will include a viewer that looks like this, with all four of your images visible.

<html>
<div style="margin: 2rem 0;">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500">
  <link rel="stylesheet" href="https://unpkg.com/mirador@latest/dist/mirador.min.css">
  
  <div id="my-mirador" style="position: relative; height: 600px; width: 100%;"></div>
  
  <script src="https://unpkg.com/mirador@latest/dist/mirador.min.js"></script>
    <script type="text/javascript">
  (function() {
    if (typeof Mirador !== 'undefined') {
      var mirador = Mirador.viewer({
        id: "my-mirador",
        manifests: {
          "https://edh.ub.uni-heidelberg.de/iiif/edh/HD005758.manifest.json": { provider: "Epigraphic Database Heidelberg" },
          "https://edh.ub.uni-heidelberg.de/iiif/edh/F030403.manifest.json": { provider: "Epigraphic Database Heidelberg" },
          "https://edh.ub.uni-heidelberg.de/iiif/edh/HD011165.manifest.json": { provider: "Epigraphic Database Heidelberg" },
          "https://edh.ub.uni-heidelberg.de/iiif/edh/F005848.manifest.json": { provider: "Epigraphic Database Heidelberg" }
        },
        windows: [
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/HD005758.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/F030403.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/HD011165.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/F005848.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' }
        ]
      });
    }
  })();
</script>
</div>
</html>


### Step 4: Initiate a pull request to submit your post

1. Once you've **Committed changes...** to your branch, you'll be prompted by GitHub to initiate a pull request to the **master** branch. Don't do so until you're sure you've got your post exactly as you want it!
2. When you do initiate a pull request, be sure that your branch is the **head** and the master branch is the **base**.
4. Name your pull request **LastName_dt2** and then click **Create pull request**.

Ok, that's it! You're done!
