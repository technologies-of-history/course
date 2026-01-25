---
layout: page
title: Digital Tools Assignment 3
permalink: /digitaltools3
---
## Making Text into Data

As you know from class, XML is a metalanguage (a language used to describe or markup another language) used in order to process and store texts in digital format. Markup languages are valuable as means of helping digital archivists and instructional technologists do two things: first, markup creates a rich data set from the text in question which can then be converted into a number of formats; second, markup encodes how a particular text should be presented on a webpage, digital publication, data set, etc. Markup languages thus guide our interpretations of those texts. Considerations like spacing, bolding, and headings are all aspects of the markup process—which is often also referred to as “encoding.” Marking up a document in XML is a matter of directing a computer as to how the manuscript’s content should be presented and interpreted.

For this assignment, you will select a page from a Middle English medical recipe collection, [Trinity College Cambridge MS O.8.35](https://mss-cat.trin.cam.ac.uk/Manuscript/O.8.35) to transcribe and encode with TEI/XML

### Trinity College Cambridge MS O.8.35, digitized by the Trinity College Cambridge Library

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
						"https://mss-cat.trin.cam.ac.uk/Manuscript/O.8.35/manifest.json": { provider: "Trinity College Cambridge" },
					},
					windows: [
						{ loadedManifest: "https://mss-cat.trin.cam.ac.uk/Manuscript/O.8.35/manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'far-bottom' },
					]
				});
			}
		})();
	</script>
</div>
</html>

### Note: Steps 1 and 2 of this Digital Tools Assignment are due March 6 at 11:59 pm

### Step 1: Transcribe a page from the manuscript

1. Click through the images of TCC MS O.8.35 and select a single page of text to transcribe. Make note of the folio number for your page, indicated at the bottom of the Mirador viewer (i.e. f001r or f014v).
2. Once you've located the folio number, visit our GitHub organization and navigate to the repository **dyngley_data**. Open the file named **iiif.xml**.
3. Scroll through the XML code under `<facsimile sameAs="https://mss-cat.trin.cam.ac.uk/Manuscript/O.8.35/manifest.json">` until you find your folio number (at the far right of each line of code). 
Each image of the manuscript has been given an xml id, which then corresponds to a folio number. For example, in this line of code 
```<surface xml:id="f016" ulx="0" uly="0" lrx="2967" lry="4062" sameAs="https://mss-cat.trin.cam.ac.uk:8183/iiif/2/O.8.35%2F017_O.8.35_f001r.jp2" ><label>f001r</label><graphic mimeType="application/json" url="https://mss-cat.trin.cam.ac.uk:8183/iiif/2/O.8.35%2F017_O.8.35_f001r.jp2"/></surface>```
the folio number of the manuscript is **f001r** (shown at the end of the URL), while the xml id that has been assigned to that folio is **f016**. That's because this is the sixteenth image in the manuscript, though it corresponds with the first official numbered folio of the manuscript.
4. Create a **.txt** file using a text editor of Google docs. Use the following naming convention: **xmlid.txt.** For example, the file featuring the transcriptions of f001r of the manuscript would be named **f016.txt.**
5. Transcribe the entire page in your text file. Be sure that you are mirroring the spelling and punctuation of your page from the manuscript **exactly.** Where there are line breaks in the manuscript, return to the next line in your **.txt** file.
6. Either save the file on your computer, or download the file from Google docs as a **.txt** file.


### Step 2: Mark-up your transcription with XML according to TEI heirarchies

1. Encode the body of the text. Your TEI encoding should follow standard format. Though the EditionCrafter workflow will create a new `<ab>` for every page of transcribed text automatically, you should still encode the text you transcribe with appropriate tags, `<title>`, `<PersonName>`, `<term>`, `<supplied>`,`<measure>`, and other tags within the TEI glossary as necessary. Please refer to the first sixteen folios of transcribed pages in **dyngley-data/transciptions** for a model of how to incorporate tags. You can also refer to the glossary of official TEI elements [here](https://tei-c.org/release/doc/tei-p5-doc/en/html/REF-ELEMENTS.html), or you can review the basic TEI tags in the [Basic Tagging tutorial](https://www.wwp.northeastern.edu/outreach/seminars/_current/presentations/basic_encoding/basic_encoding_tutorial_00.xhtml) from the Women Writer's Project.
2. Check the order and hierarchy of your code. Are all open elements closed again? Are elements nested properly? Copy and paste your TEI into [Code Beautify](https://codebeautify.org/xmlvalidator) if you'd like to check for open tags and broken elements.
3. Finally, once you're sure you've got the TEI *and* transcription right, it's time to upload your transcription to the repository **dyngley-data** in our GitHub organization so that I can include your work in the [critical edition of TCC MS O.8.35](https://cu-mkp.github.io/dyngleyfamily-editioncrafter-website/folios/#/ec)!
4. Fork the **dyngley-data** repository into your own account. Locate the **transcriptions** folder within that forked repository. Click **Add file** and upload your **.txt** file with your transcription and XML. Finish by submitting a pull request to the **technologies-of-history/dyngley-data** repository.
5. Once I've looked over your transcription, I'll merge your pull request and then run EditionCrafter to incorporate your transcription into our digital edition.

**Note**: *If you'd like more information on how EditionCrafter works to combine the XML of your marked-up transcription with the XML of the IIIF manifest, you can read about that [here](https://editioncrafter.org/guide/#creating-a-tei-document-from-your-iiif-manifest). I'm also happy to explain it in more detail in class, though I'm not the developer!*

### Step 4: Explain yourself

1. Draft a post following our course protocols (open or fork the **spring-2026** repository in your account, navigate to the **_posts** folder and create a new .md file titled **yyyy-mm-dd-your title.md**, or draft the post in Google docs and then download and upload the **.md** file) and include the appropriate YAML header. 
2. Somewhere in your post you should copy your transcription and TEI encoding from your .txt file. You'll want to set off your mark-up to show up as code on our blog, which means you'll need to use the appropriate Markdown syntax. (Hint: bracket your marked-up transcription with triple ticks at the start and at the end. You can always refer back to the [Getting Started with Markdown](https://programminghistorian.org/en/lessons/getting-started-with-markdown) lesson you completed at the start of the semester.)
3. In the same .md file, write a 4-5 paragraph blog post responding to the following questions:

- Why did you choose the page that you did? What recipes were in your transcription?
- What was the process of learning to transcribe Middle English like?
- What questions do you have about the act of recording this recipe in a manuscript?
- What aspects of the document does TEI make more visible to a future researcher?
- How does encoding the text transform its utility?
- What questions about the relationship between technical writing and making emerged in this process?

### Step 5: Submission

Finish by submitting a **pull request** to the **technologies-of-history/spring-2026** repository. Name the pull request **lastname-dt3**. That's it!
