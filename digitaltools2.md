---
layout: page
title: Digital Tools Assignment 2
permalink: /digitaltools2
---
## Showing History

Now that you've mastered the work flow of forking from our repository, creating a file, writing a post in Markdown format, committing your changes, and creating a pull request, you're ready to begin to create digital historical scholarship incorporating other digital tools.

### Step 1: Visit the [Heidelberg Epigraphic Database](https://edh.ub.uni-heidelberg.de/foto/suche)

After browsing the examples of surviving Roman epigraphy compiled on the site, choose four to focus on for your second digital tools assignment (these may be the same four you worked with in class). Your post will compare these four examples, describing what each inscription says, where it is found, when it was created, and finally, how each reveals something about the status and function of public writing in Roman society. 

### Step 2: Create your Google MyMaps



### Step 3: Create a new blog post

1. Draft a post following our course protocols (create a new branch in **spring-2026** called **lastname-dt2**, navigate to **_posts** and create a new .md file titled **yyyy-mm-dd-your title.md**.) 
2. Be sure your .md includes the following header:

 ```
 ---
 layout: post
 title: [Your title here]
 ---
 ```

3. Draft a 3-4 paragraph post that introduces your four examples of epigraphic inscriptions, including their date, their location, a transcription, and their significance. Reflect on how these surviving examples of public writing shed light on the social fabric and culture of the vast Roman empire. You may wish to think about the distance or time separating some of the inscriptions; or you may wish to reflect on the permanence of this sort of writing; or you may wish to reflect on differences you see in style or content of your inscriptions.

### Step 5: Embed the Mirador IIIF viewer to show your inscriptions

Your blog post should include images of the four inscriptions you've chosen to analyze. To include those images in your post, we're not going to host those images in our site repository, as that would lead to . We're going to embed a IIIF viewer to load the JSON manifests of those images and enable manipulation of the images on our site. The easiest way to do this is to embed a Mirador Viewer in to your blog post by copying the following code into your blog post. 

```
< html >
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
          "https://edh.ub.uni-heidelberg.de/iiif/edh/F002574.manifest.json": { provider: "Epigraphic Database Heidelberg" },
          "https://edh.ub.uni-heidelberg.de/iiif/edh/F002710.manifest.json": { provider: "Epigraphic Database Heidelberg" },
          "https://edh.ub.uni-heidelberg.de/iiif/edh/F002292.manifest.json": { provider: "Epigraphic Database Heidelberg" },
          "https://edh.ub.uni-heidelberg.de/iiif/edh/F002909.manifest.json": { provider: "Epigraphic Database Heidelberg" }
        },
        windows: [
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/F002574.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/F002710.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/F002292.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/F002909.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' }
        ]
      });
    }
  })();
</script>
</div>
< /html >
```

### Step 6: Change out the IIIF Manifests to *Your* Images

1. Each image in the Epigraphic Heidelberg Database includes a link (just below the image viewer) to a IIIF manifest. Click the link, and you'll see a webpage that looks like nothing but Javascript code.
2. Copy the URL to that webpage with nothing but text. It will end with **...manifest.json**
3. Paste that URL so that it replaces the first URL within quotations under both `manifests:` and `windows:`. Make sure your URL is bracketed by double quotations, just as you see in the example above.
4. Continue the process for the next three IIIF manifests, eventually replacing all of the URLS to IIIF manifests in the example above to your own images.

If you've done it correctly, your post will include a viewer that looks like this, with all four of your images visiable.

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
          "https://edh.ub.uni-heidelberg.de/iiif/edh/F002574.manifest.json": { provider: "Epigraphic Database Heidelberg" },
          "https://edh.ub.uni-heidelberg.de/iiif/edh/F002710.manifest.json": { provider: "Epigraphic Database Heidelberg" },
          "https://edh.ub.uni-heidelberg.de/iiif/edh/F002292.manifest.json": { provider: "Epigraphic Database Heidelberg" },
          "https://edh.ub.uni-heidelberg.de/iiif/edh/F002909.manifest.json": { provider: "Epigraphic Database Heidelberg" }
        },
        windows: [
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/F002574.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/F002710.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/F002292.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' },
          { loadedManifest: "https://edh.ub.uni-heidelberg.de/iiif/edh/F002909.manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'none' }
        ]
      });
    }
  })();
</script>
</div>
</html>


### Step 6: Embed your Google MyMaps to demonstrate their location


### Step 7: Submit your post

1. After you create this Markdown file and fill it with your content, **Commit changes...** to save the file to your branch. Every time you do something in the file, you'll write up a brief description of what you changed and click, **Commit** to save. Be sure to select the option to commit to **your** new branch, **lastname-dt1**.
1. Click **spring-2026** to return to the main repository.
2. Be sure to check and make sure you're in your **lastname-dt1** branch.
3. In the menu at the top of the page, click **Pull requests**. 
2. Click the green button **New pull request**. 
3. You'll now see a gray box at the top that shows you the **base** repository you'll be sending your changes to and the **head** repository, which is yours. NOTE: Be sure that yours is the **head** and the main branch is the **base**.
4. Name your pull request **LastName_dt2** and then click **Create pull request**.

Ok, that's it! You're done!
