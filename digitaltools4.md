---
layout: page
title: Digital Tools 4
permalink: /digitaltools4
---

# Mapping History

You’ve already embedded an interactive map in your second Digital Tools assignment. Now, for your fourth Digital Tools Assignment, you will use a more robust mapping tool to create a visual and spatial historical narrative. [ArcGIS Online](http://tcugis.maps.arcgis.com) is an online interface for creating Geographical Information Systems (GIS). GIS is a means of connecting data to a map, integrating location data (where things are) with all types of descriptive information (what things are like there). It does so by presenting data as layers that can be visualized on a base map. For this assignment, you'll create one of those layers by georeferencing an early printed map from [Old Maps Online](https://www.oldmapsonline.org/) to present geospatial data on a singular voyage of discovery (gathered from the [Age of Exploration](https://resources.amdigital.co.uk/aoe/map/) site) by creating and sharing your own ArcGIS Story Map.

We'll work together on Steps 1 and 2 of this assignment in class on Thursday, March 26. This assignment is due on GitHub by 11:59 pm on Friday, April 3.

## Step 1: Choose a Voyage Dataset

1. Visit the [Age of Exploration](https://resources.amdigital.co.uk/aoe/map/) site and explore the voyages of discovery that are mapped there. Decide which voyage you want to work with for this assignment. 
2. To access the geo coordinate data for this assignment, you'll click **Dowload Data** at the top right of the [Age of Exploration](https://resources.amdigital.co.uk/aoe/map/) site. The webpage that appears contains *all* the data from this project.
2. Right click the webpage and click **Save As...**. Save the file somewhere on your computer, making sure you add **.csv** to the end of the filename.
3. Double check that you've created the file correctly by opening the **.csv** file you created (in Excel or Google sheets). Once the file is open, you can delete all the data you **don't** need, keeping only the coordinates and dates for your chosen voyage.

## Step 2: Choose a Historical Map to GeoReference
1. Now that your dataset is selected, visit [Old Maps Online](https://www.oldmapsonline.org/) to find a historical map that matches the region and era of your voyage. For example, if you've selected Captain Cook's first voyage, you might want to find a map of Polynesia and Australia from the early 1800s.
2. You can find a map that fits the bill by using the bottom timeline slider to adjust the era of map you're looking for, and then changing the map view to focus on the area of the globe you'd like to see maps for. Make sure the map you choose is from the **David Rumsey Collection** (you can tell because you'll see the black box with the David Rumsey logo next to the map image.) Click the **Docuemnt** tab in the menu above your map to view its full title. This will be helpful in a minute.
3. After finding a map to work with in [Open Maps Online](https://www.oldmapsonline.org/), navigate to [David Rumsey Map Collection](https://www.davidrumsey.com) and copy-and-paste the title of the map you've selected into the search box. You should see it appear in search results.
4. Once you've located your map on the [David Rumsey Map Collection](https://www.davidrumsey.com), click **Share** in the menu at the top of the page, and then select **IIIF Manifests**. You'll see a URL there to the image manifest. Click the icon to the right to copy it to your clipboard.

## Step 3: Georeference and Warp your Map with AllMaps
1. Visit [AllMaps](https://editor.allmaps.org), a site that takes advantage of IIIF format and JavaScript to enable map warping that is easily done browser-side. Paste the URL to your map's IIIF manifest in the input box.
2. You should see your map image appear with a blue background. You'll see a menu at the top of the page that walks you through the steps to Geowarp your map: Image-->Draw Mask-->Georeference-->Results. Click **Draw Mask.**
3. Use your mouse to select the area of your image you want to treat as a map. For example, if your map was printed in a book with text and a wide border, you may want to draw your mask to exclude that stuff. Double click your last point when you're satisfied with your mask.
4. Now click over to **Georeference.** You'll see a split screen view with your map image on the left and a world map on the right. Your job is now to find a point in your image and match it to the same point on the world map. Just click one, then click the other. Do this over and over until you've worked your way around your map, identifying as many points as you can. To check your work, click the options icon (the little cog thingy at top right) and increase the opacity of the image. You'll see your image overlayed on the world map.
5. Once you're satisfied with the map warp, click **Results.** This will show you your map in its correct place. Click **Export** at the top right. You'll see three URLs; you want the last one. Click the icon next to the **XYZ Map Tiles** URL to copy it to your clipboard.

## Step 4: Import your map into ArcGIS

1. Log into [ArcGIS Online](http://tcugis.maps.arcgis.com). In the menu at the top of the page, click **Map**.
2. You'll see a new screen with a world map and two menus, one to the right and one to the left. In the left-hand menu, click **Layers.**
3. Click the drop-down arrow and select **Add layer from URL**. 
4. In the input box that appears, paste the URL from AllMaps. ArcGIS should immediately recognize it as a Tile Layer.
5. Name your map with the title of the map from David Rumsey Maps, and be sure to attribute it to that site. Click **Add to Map.**
6. You should see your georeferenced map wherever it should be on the world map! Congrats! You may want to play around with the base map, though I like the topographical map that appears standard.
7. Finally, in the left-hand menu, click **Save and Open**, then **Save As** and save this map to your account. You can name it Digital Tools 4.

## Step 5: Create your Story Map with ArcGIS

1. Visit [storymaps.arcgis.com](https://storymaps.arcgis.com) and log in using your username and password for ArcGIS. 
2. Create a new Story Map, titling it whatever seems best for your particular voyage of exploration. Click the plus sign to add an element and scroll down to select **Map Tour**. Select **Start from Scratch** and then select a **Map Focused Guided Tour**, the option on the top left.
3. Click the pencil icon in the map section of your StoryMap. When the new map menu opens, click the box under **Select basemap** and select **Browse more maps**. This should bring you to a page with your saved content, where you can select your saved georeferenced historical map.
4. Now you can create a StoryMap with the coordinates of your selected voyage of exploration. Each coordinate should be one a slide in the story. You'll add a location for a each slide (type the coordinates into the search bar for that point, then click Add to Map), and upload a photo (use your imagination) and a brief decription of that stage of your chosen voyage.
5. Once you're finished with your StoryMap, you'll need to **Publish** it so that it can be embedded in your post. Be sure to select **Public** from the dropdown menu, but you can deselct "Allow duplication" and "Show in Web Search Results."
6. Once your StoryMap is published, open up your StoryMap to view it, and click the three dots in the topbat menu at the far right. Select **Embed this story** and then copy the code that appears.

## Step 6: Compose your post
1. Create a Markdown file according to our course protocols (fork or open the **spring-2026** repository in your personal account, locate the **_posts** folder, and create or upload a file named **YYY-MM-DD-Your Title.md.**) *Note: Do not name your file Digital Tools 4. We can't have multiple files merged with the same filename. They'll overwrite one another once I merge your post into the course repo. Think of something more creative!*
2. Compose a 3-4 paragraph post responding to the following question:
- What boyage of exploration did you choose and why?
- How does your historical map reflect the scope of geographic knowledge, navigational skill, and cartographic expertise at the time of your chosen voyage?
- How did your particular voyage of exploration transform the way the world was understood and depicted at the time?
- In your opinion, have digital tools for map-making and geocoding, captured in Geographic Information Systems, transformed the way we understand visualize and understand human interaction with the physical world in the same ways as 'tracks on the ocean' as described by Sara Caputo?
3. Decide where you'd like your StoryMap to appear in your post, and then paste the embed code you copied from ArcGIS online, making sure to wrap the code in `<html>` tags.

## Step 7: Submit your post
Commit your changes and submit a pull request to **technologies-of-history/spring-2026**, and you're done!
