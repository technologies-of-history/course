---
layout: page
title: Digital Tools Assignment 2
permalink: /digitaltools2
---
## Showing History

Now that you've mastered the work flow of forking from our repository, creating a file, writing a post in Markdown format, committing your changes, and creating a pull request, you're ready to begin to create digital historical scholarship incorporating other digital tools.

### Step 1: Visit the Heidelberg Epigraphic Database

1. Browse the selection of ancient Roman epigraphy that appears when you choose a single Roman province from the drop-down menu in the [photographic database](https://edh.ub.uni-heidelberg.de/foto/suche) search page. After perusing the selection from different provinces, choose one province to work with. For the purposes of this exercise, you should choose a province with no more than 350 or so results.
2. Run a search for inscriptions from your chosen province, and click the option at the bottom to **sort by** and select **HD no.** 
3. Once you've selected your province and generated the search results, you'll see a link at the top of the page (above the list of results) with a link to download the results as a **.csv file.** Click the link to download the file, then save it on your computer.
4. Next, select four inscriptions from the results that appear for your chosen Roman province, making sure that the inscriptions you pick have good quality images and that the have an **HD number** link. I'd suggest picking a range of inscriptions that include both formal epigraphy and informal graffiti-style carving. For each of the inscriptions you've chosen, click the **HD number** link and keep the page open on your browser. You'll need it in a few steps.

### Step 2: Create a new Markdown file for your post

1. Draft a post following our course protocols (create a new branch in **spring-2026** called **lastname-dt2**, navigate to **_posts** and create a new .md file titled **yyyy-mm-dd-your title.md**.) 
2. Be sure your .md includes the following header:

 ```
 ---
 layout: post
 title: [Your title here]
 ---
 ```

### Step 3: Embed the Mirador IIIF viewer to show your inscriptions

Your blog post should include images of the four inscriptions you've chosen to analyze. To include those images in your post, we're going to embed a IIIF viewer to load the JSON manifests of those images and enable manipulation of the images on our site. The easiest way to do this is to embed a Mirador Viewer in to your blog post by copying the following code into your blog post. 

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
          "https://edh.ub.uni-heidelberg.de/iiif/edh/HD005758.manifest.json": { provider: "Epigraphic Database Heidelberg" },
          "https://edh.ub.uni-heidelberg.de/iiif/edh/HD046143.manifest.json": { provider: "Epigraphic Database Heidelberg" },
          "https://edh.ub.uni-heidelberg.de/iiif/edh/HD011165.manifest.json": { provider: "Epigraphic Database Heidelberg" },
          "https://edh.ub.uni-heidelberg.de/iiif/edh/F005848.manifest.json": { provider: "Epigraphic Database Heidelberg" }
        },
        windows: [
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/HD005758.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/HD046143.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/HD011165.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/F005848.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' }
        ]
      });
    }
  })();
</script>
</div>
</html>
```

### Step 4: Change out the IIIF Manifests to *Your* Images

1. Each image in the Epigraphic Heidelberg Database includes a link to a IIIF manifest. In the four browser windows you still have open for the four images you've chosen, click the **IIIF Manifest** link to view the JSON manifest. 
2. Copy the URL to the webpage that opens with the Javascript code. It will end with **...manifest.json**
3. Paste that URL so that it replaces the first URL within quotations under both `manifests:` and `windows:`. Make sure your URL is bracketed by double quotations, just as you see in the example above.
4. Continue the process for the next three IIIF manifests, eventually replacing all of the URLS to IIIF manifests in the example above to your own images.

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

### Step 5: Create your Google MyMaps
1. Open the **.csv file** that you downloaded from the Heidelberg Epigraphy Database. Sort the data according to **modern find spot** so that the same places are grouped together. 
2. Open a new spreadsheet on your computer. Copy-and-paste the **modern find spots** column from the original file into the first column of the new spreadsheet, followed by the **country** column in the next column, and finally, in the fhird column, paste in the column **ancient find spot**. Double check that the appropriate ancient name matches the modern name in this new spreadsheet by cross-referencing against the original file. Save the spreadsheet on your computer as a **.csv file.**
3. Next, navigate to [Google My Maps](https://mymaps.google.com). Log in if you haven't, and click **Create New Map.**
4. Name your map, and then click **Import**. Drag and drop your new **.csv file** with the three columns of place names. Select the **modern find spot** and **country** as the two columns MyMaps should use to generate places on the map. Select **ancient find spots** as the column MyMaps should use to name the places.
5. Play around with the styling and background until the map looks the way you'd like.
6. Click **share** in the My Maps menu, and share the map via your Google drive. No need to email it to anyone. Once your map is public, you can click the three dots at the top right of the MyMaps menu and select **Embed on my site.**
7. Copy and paste the code that is generated into the body of your post, making sure you wrap the code in `<html> </html>` tags.

### Step 6: Draft your post

Now that you've got the code for a Mirador viewer and Google MyMaps copied into your post, it's time to compose a 3-4 paragraph post responding to the following prompt: (Note: you can add Markdown language before and after your embedded code, so please do use your own words to introduce the images and map.)

Referencing the transcriptions and images for your four inscriptions on the Heidelberg Epigraphic Database, Cooley and Bispham's chapter, and your map illustrating the geographic distribution of epigraphic writing in your chosen province, what do these pieces of evidence tell us about Roman attitudes toward public writing? In what ways do you think digital archives and repositories may have changed how we understand writing in Roman culture?

### Step 7: Submit your post

1. After you create this Markdown file and fill it with your content, **Commit changes...** to save the file to your branch. Every time you do something in the file, you'll write up a brief description of what you changed and click, **Commit** to save. Be sure to select the option to commit to **your** new branch, **lastname-dt1**.
1. Click **spring-2026** to return to the main repository.
2. Be sure to check and make sure you're in your **lastname-dt1** branch.
3. In the menu at the top of the page, click **Pull requests**. 
2. Click the green button **New pull request**. 
3. You'll now see a gray box at the top that shows you the **base** repository you'll be sending your changes to and the **head** repository, which is yours. NOTE: Be sure that yours is the **head** and the main branch is the **base**.
4. Name your pull request **LastName_dt2** and then click **Create pull request**.

Ok, that's it! You're done!
