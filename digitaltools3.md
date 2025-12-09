---
layout: page
title: Digital Tools Assignment 3
---
## Turning texts into data with XML and EditionCrafter

As you know from class, XML is a metalanguage (a language used to describe or markup another language) used in order to process and store texts in digital format. Markup languages are valuable as means of helping digital archivists and instructional technologists do two things: first, markup creates a rich data set from the text in question which can then be converted into a number of formats; second, markup encodes how a particular text should be presented on a webpage, digital publication, data set, etc. Markup languages thus guide our interpretations of those texts. Considerations like spacing, bolding, and headings are all aspects of the markup process—which is often also referred to as “encoding.” Marking up a document in XML is a matter of directing a person as to how the manuscript’s content should be presented and interpreted.

For this assignment, you will select a Middle English medical recipe from [Trinity College Cambridge MS O.8.35](https://mss-cat.trin.cam.ac.uk/Manuscript/O.8.35) in order to create your own TEI markup.

## Trinity College Cambridge MS O.8.35, digitized by the Trinity College Cambridge Library

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

## Step 1: Transcribe a page of text

1. Click through the images of TCC MS O.8.35 and select a single page of text to transcribe. Make note of the folio number for your page, indicated at the bottom of the Mirador viewer (i.e. f001r or f014v).
2. Once you've located the folio number, visit our GitHub organization and navigate to the repository **dyngley_data**. Open the file named **dyngley.xml**.
3. Scroll through the XML code under `<facsimile sameAs="https://mss-cat.trin.cam.ac.uk/Manuscript/O.8.35/manifest.json">` until you find your folio number. 
Each image of the manuscript has been given an xml id, which then corresponds to a folio number. For example, in this line of code 
```<surface xml:id="f016" ulx="0" uly="0" lrx="2967" lry="4062" sameAs="https://mss-cat.trin.cam.ac.uk:8183/iiif/2/O.8.35%2F017_O.8.35_f001r.jp2" ><label>f001r</label><graphic mimeType="application/json" url="https://mss-cat.trin.cam.ac.uk:8183/iiif/2/O.8.35%2F017_O.8.35_f001r.jp2"/></surface>```
the xml id is "f016" while the actual folio number of the manuscript is "f001r."
That's because this is the sixteenth image in the manuscript, though it corresponds with the first official numbered folio of the manuscript.
4. Create a **.txt** file using your text editor. Use the following naming convention: **the_xml_id_for_your_page.txt.** For example, the file featuring the transcriptions of f001r of the manuscript would be named **f016.txt.**
5. Transcribe the entire recipe in your text file. Be sure that you are mirroring the spelling and punctuation of your page from the manuscript **exactly.** Where there are line breaks in the manuscript, return to the next line in your .txt file.

Once I've looked over your transcription, I'll merge your file into the larger XML file for the critical edition.


## Step 2: Mark-up your transcription using TEI in Markdown

1. Encode the body of the text. Your TEI encoding should follow standard format. Though the EditionCrafter workflow will create a new `<div>` for every page of transcribed text automatically, you should still encode the text you transcribe with appropriate tags, `<title>`, `<PersonName>`, and `<measure>` and other tags within the TEI glossary as necessary. You can refer to the glossary of official TEI elements [here](https://tei-c.org/release/doc/tei-p5-doc/en/html/REF-ELEMENTS.html), or you can review the basic TEI tags in the [Basic Tagging tutorial](https://www.wwp.northeastern.edu/outreach/seminars/_current/presentations/basic_encoding/basic_encoding_tutorial_00.xhtml) from the Women Writer's Project.
2. Check the order and hierarchy of your code. Are all open elements closed again? Are elements nested properly? Copy and paste your TEI into [Code Beautify](https://codebeautify.org/xmlvalidator) if you'd like to check for open tags and broken elements.
3. Finally, once you're sure you've got the TEI right, link to the actual folio in the [critical edition of TCC MS O.8.35](https://cu-mkp.github.io/dyngleyfamily-editioncrafter-website/folios/#/ec) that features your transcription!
4. Upload your .txt file to the **dyngley-data** repository in our GitHub organization, in the folder **transcriptions**, following our GitHub submission protocols. Create a branch in the **dyngley-data** repository named **yourlastname_transcription**. Upload the file to the **transcriptions** folder within that branch. Finish by submitting a pull request to the **master** branch of our repository. 


## Step 3: Explain yourself

1. Draft a post following our course protocols (make a new branch in **spring-2026** called **lastname-dt3**, navigate to the **_posts** folder and create a new .md file titled **yyyy-mm-dd-your title.md**.) 
2. Be sure your .md includes the following header:
 ```
 ---
 layout: post
 author: Your Name Here
 title: Your title here
 excerpt_separator: <!--more-->
 ---
 ```
 
3. Somewhere in that .md file, copy your transcription text from your .txt file. You'll want to set off your mark-up to show up as code on our blog, which means you'll need to use the appropriate Markdown syntax to set off your code from the rest of your blog post. (Hint: bracket your marked-up transcription with triple ticks at the start and at the end. You can always refer back to the [Getting Started with Markdown](https://programminghistorian.org/en/lessons/getting-started-with-markdown) lesson you completed at the start of the semester.)
4. In the same .md file, write a 4-5 paragraph blog post responding to the following questions:

- What sort of recipe did you choose, and why?
- What was the process of learning to transcribe Middle English like?
- What questions do you have about the act of recording this recipe in a manuscript?
- What aspects of the document does TEI make more visible to a future researcher?
- How does encoding the text transform its utility?
- What questions about the relationship between technical writing and making emerged in this process?

## Step 4: Submission

Finish by submitting a **pull request** to the **master** branch of our class repository.

## An example of the TEI markup for the first folio of the [critical edition of TCC MS O.8.35](https://cu-mkp.github.io/dyngleyfamily-editioncrafter-website/folios/#/ec):


```
<pb facs="#f016" />
<ab>
<div>
	<head>
	<handShift/>
	<title>of all maner of Infyrmytes</title>
 	<handShift/>
 	</head>
 	<p>Here begynneth a tretys of al manere of infirmitees of mannys body. 
 	bothe withinne as touchyng to phisyke and withoute as touching to surgerie 
 	from the croune of the heed to the sool of the foot. And the remedies therwith 
 	if god wol. And furst we wol at heer of the hed how it shulde be norisshede &amp; kepte &amp;c.</p>
</div>
<div>
	<head>
	<title>For to make heer to growe.</title>
	</head>
	<p>Take withien leves and sethe hem in oyle and hony and anoynte the heede 
	therwith. and it shal make the heer to growe and waxe. 
	<title>Another.</title> Take beer &amp; drie hem in a furneys or in a panne
	and make therof a pouder. and sethe it in hony and anoynt the pacient therwith and it schal 
	make the heer to growe. <title>Another.</title> forto make heer to growe after scalles. 
	There is an oynement that is cleped <term>unguentum <persName>aristotilis</persName></term>. 
	thus it must be made. Take the sewet of a dere either fresshe shepys talu and 
	pich that is fletyng. oyle olyf and gret salt. of iche of these <measure>iii. unces</measure> 
	or <measure>half a quartron</measure> of white waxe <measure>half an unce</measure>. 
	than first take the sewt. or </p>
  </div>
  </ab>
```
