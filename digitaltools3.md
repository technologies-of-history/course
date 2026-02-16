---
layout: page
title: Digital Tools Assignment 3
permalink: /digitaltools3
---
# Making Text into Data

As you know from class, XML (eXtensible Markup Language) is a metalanguage (a language used to describe or markup another language) used in order to process and store data. Markup languages are valuable as means of helping digital archivists and instructional technologists do two things: first, markup creates a rich data set from the text in question which can then be converted into a number of formats; second, markup encodes how a particular text should be presented on a webpage, digital publication, data set, etc. Marking up a document in XML is a matter of directing a computer as to how the manuscript’s content should be presented and interpreted. Decades ago, the [Text Encoding Initiative](https://tei-c.org) (TEI) was developed to standardize how digital humanists encoded texts. 

For this assignment, you'll be adding limited XML to a page of Middle English medical recipes that you'll transcribe from [Trinity College Cambridge MS O.8.35](https://mss-cat.trin.cam.ac.uk/Manuscript/O.8.35), a mid-fifteenth-century English compendium of medical knowledge. Your marked-up transcription will then get added to the digital critical edition of the manuscript, [Old Books, New Science](https://technologies-of-history.github.io/dyngley-edition), created using [EditionCrafter](https://editioncrafter.org), an open-access tool that marries XML encoded text to images served in IIIF. 

I'll assign your page of text in class on Tuesday, February 17, and you'll work with your classmates on Thursday, February 19 to complete your transcription.

We'll work together on Steps 1 and 2 of this assignment on Thursday, February 19 and Thursday, February 26. Steps 1, 2, and 3 are due March 6 at 11:59 pm; Step 4 is due by March 13 at 11:59 pm.

## Trinity College Cambridge MS O.8.35, digitized by the Trinity College Cambridge Library

<html>
<div style="margin: 2rem 0;">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500">
  <link rel="stylesheet" href="https://unpkg.com/mirador@latest/dist/mirador.min.css">
  
  <div id="my-mirador" style="position: relative; height: 600px; width: 100%;"></div>
  
  <script src="https://unpkg.com/mirador@latest/dist/mirador.min.js"></script>
  <script type="text/javascript">
        const mirador = Mirador.viewer({
          id: "my-mirador",
          manifests: {
						"https://mss-cat.trin.cam.ac.uk/Manuscript/O.8.35/manifest.json": { provider: "Trinity College Cambridge" },
					},
					windows: [
						{ loadedManifest: "https://mss-cat.trin.cam.ac.uk/Manuscript/O.8.35/manifest.json", canvasIndex: 0, thumbnailNavigationPosition: 'far-bottom' },
					]
				})();
	</script>
</div>
</html>


## Step 1: Transcribe a page of a fifteenth-century manuscript

First, visit the **dyngley_data** repository in our GitHub organization. Open the file named **dyngley.xml**. You'll notice that each image of the manuscript has been given an **xml id**, which then corresponds to a folio number in the manuscript. For example, in this line of code 
`<surface xml:id="f016" ulx="0" uly="0" lrx="2967" lry="4062" sameAs="https://mss-cat.trin.cam.ac.uk:8183/iiif/2/O.8.35%2F017_O.8.35_f001r.jp2" ><label>f001r</label><graphic mimeType="application/json" url="https://mss-cat.trin.cam.ac.uk:8183/iiif/2/O.8.35%2F017_O.8.35_f001r.jp2"/></surface>` the folio number of the manuscript is **f001r** (shown at the end of the URL), while the xml id that has been assigned to that folio is **f016**, right at the beginning of this line of code. That's because this is the sixteenth image in the manuscript, though it corresponds with the first official numbered folio of the manuscript.

Each of you is assigned one page of the manuscript to transcribe for your this digital tools assignment. Consult the table below to find your assigned page and the correspinding XML ID that matches that page. To begin transcribing your page of the manuscript, open a Google doc and name your doc **fxmlid** (so, for example, folio 1r of the manuscript, referenced above, would be titled **f016**). 

In the Google doc you've created, you will transcribe the entire page you've been assigned.  You'll be sure to hit enter to create a line break whenever there's a line break in the manuscript. You'll also be sure to mirror the spelling and punctuation that you see *exactly*. This will be difficult! The best way to get better is to keep trying. I encourage you to try your best to get a rough draft, then swap with a partner and have them read what you've done and offer suggestions.

| **Student** | **Manuscript Page** | **XML ID** |
| :--- | ---: | ---: |
| Jane Allinger | f. 64r | f142 |
| Fiona Corrigan | f. 64v | f143 |
| Camila Erazo | f. 65r | f144 |
| Hudson Hahn | f. 65v | f145 |
| Stella Lenzie | f. 66r | f146 |
| Kasia Love | f. 66v | f147 |
| Jonathan Martinez | f. 67r | f148 |
| Kylie Millar | f. 67v | f149 |
| Aiden Reed | f. 68r | f150|
| Keilah Scott | f. 68v | f151 |
| David Smith | f. 69r | f152 |
| Andrew Stillwell | f. 69v | f153 |
| Hailey Stuart | f. 70r | f154 |
| Katie Tovar | f. 70v | f155 |
| Vivian Velasquez | f. 71r | f156 |


## Step 2: Mark-up your transcription with XML according to TEI heirarchies

The EditionCrafter workflow will automatically create a TEI header and a number of other XML tags to merge these separate txt files into one XML file, so you don't need to open your transcription with a `<p>` or `<ab>` tag. However, you should still add internal tags to the text you transcribe when necessary. The following tags are included in the TEI header:
- `<title>`: denotes the title of a recipe
- `<PersonName>`: exactly what it sounds like
- `<term>`: these tags should be wrapped in `<ref>` tags, and they are uncommon. They indicate a word that should be included in an eventual glossary because they are unusual or unique.
- `<supplied>`: should be used when *you* add something to the transcription that isn't entirely indicated in the manuscript. These are uncommon tags, and you do not add then when you simply extend a common abbreviation. 
- `<measure>`: indicates a unit of measurement in the recipe
- `<time>`: indicates when a length of time is referenced in the recipe 

Please refer to the first sixteen folios of transcribed pages in **dyngley-data/transciptions** for a model of how to incorporate tags. You can also refer to the glossary of official TEI elements [here](https://tei-c.org/release/doc/tei-p5-doc/en/html/REF-ELEMENTS.html), or you can review the basic TEI tags in the [Basic Tagging tutorial](https://www.wwp.northeastern.edu/outreach/seminars/_current/presentations/basic_encoding/basic_encoding_tutorial_00.xhtml) from the Women Writer's Project.

Check the order and hierarchy of your code. Are all open elements closed again? Are elements nested properly? Copy and paste your TEI into [Code Beautify](https://codebeautify.org/xmlvalidator) if you'd like to check for open tags and broken elements.


## Step 3: Submit your transcription with a pull request
1. Once you're sure you've got the TEI *and* transcription right, it's time to add your transcription to the **dyngley-data** repository in our GitHub organization so that I can include your work in the [critical edition of TCC MS O.8.35](https://technologies-of-history.github.io/dyngley-edition).
2. Just as we did with the **spring-2026** repository, you'll create a new branch in the **dyngley-data** repository named **lastname-dt3**. Next, locate the **transcriptions** folder within that branch. Click **Add file** and upload your **.txt** file with your transcription and XML. 
3. Finish by submitting a pull request to the **main** branch of the **dyngley-data** repository. Once I've looked over your transcription, I'll merge your pull request and then run EditionCrafter to incorporate your transcription into our digital edition.

**Note**: *If you'd like more information on how EditionCrafter works to combine the XML of your marked-up transcription with the XML of the IIIF manifest, you can read about that [here](https://editioncrafter.org/guide/#creating-a-tei-document-from-your-iiif-manifest). I'm also happy to explain it in more detail in class, though I'm not the developer who wrote the program!*

## Step 4: Explain yourself

1. Create a Markdown file following our course protocols (open or fork the **spring-2026** repository in your account, navigate to the **_posts** folder and create a new .md file titled **yyyy-mm-dd-your title.md**, or draft the post in Google docs and then download and upload the **.md** file) and include the appropriate YAML header. *Note: Do not name your file Digital Tools 3. We can't have multiple files merged with the same filename. They'll overwrite one another once I merge your post into the course repo. Think of something more creative!*
2. Somewhere in your post, copy your transcription and TEI encoding from your .txt file. Set off your mark-up with triple ticks so that it will show up as code in yout post.
3. In the same .md file, write a 3-4 paragraph blog post responding to the following questions:

- What recipes were in your transcription?
- What was the process of learning to transcribe Middle English like?
- What questions do you have about the act of recording this recipe in a manuscript?
- How might encoding the text with XML mark-up transform its utility?
- According to Pamela Smith, communicating embodied knowledge in writing required acts of translation: taking tacit knowledge and making it explicit. In what ways does the act of encoding text with XML tags mirror the process of 'translation' decribed by Smith? 

## Step 4: Submission

Finish by submitting a **pull request** to the **technologies-of-history/spring-2026** repository. Name the pull request **lastname-dt3**. That's it!
