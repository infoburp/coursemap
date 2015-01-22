//set up the diameter of the main circle.
var diameter = Math.min(Math.max(document.documentElement.clientWidth, window.innerWidth || 0), Math.max(document.documentElement.clientHeight, window.innerHeight || 0));
//set up colours.
var color = d3.scale.linear()
    .domain([-1, 5])
    .range(["hsl(0%,0%,90%)", "hsl(0%,0%,30%)"])
    .interpolate(d3.interpolateHcl);
//set up node packing
var pack = d3.layout.pack()
    .padding(2)
    .size([diameter, diameter])
    .value(function(d) { return d.size; })
//set up the SVG that will hold the visualisation
var svg = d3.select("body").append("svg")
    .attr("width",Math.max(document.documentElement.clientWidth, window.innerWidth || 0))
    .attr("height", diameter)
  .append("g")
    .attr("transform", "translate(" + Math.max(document.documentElement.clientWidth, window.innerWidth || 0) / 2 + "," + diameter / 2 + ")");
//load in some json data
d3.json("sampledata.json", function(error, root) {
  if (error) {
    return console.error(error);
  }
//set up various variables.
var focus = root;
var nodes = pack.nodes(root);
var view;
//set up the circles
var circle = svg.selectAll("circle")
  .data(nodes)
    .enter().append("circle")
    .attr("class", function(d) { return d.parent ? d.children ? "node" : "node node--leaf" : "node node--root"; })
  .style("fill", function(d) { return d.children ? color(d.depth) : null; })
    .on("click", function(d) { if (focus !== d) zoom(d), d3.event.stopPropagation(); });
//set up the text inside circles
var text = svg.selectAll("text")
  .data(nodes)
    .enter().append("text")
    .attr("class", "label")
  .style("fill-opacity", function(d) { return d.parent === root ? 1 : 0; })
  .style("display", function(d) { return d.parent === root ? null : "none"; })
  .text(function(d) { return d.name; });
//set up nodes
var node = svg.selectAll("circle,text");
//set up style, and interaction handler
d3.select("body")
  .style("background", color(-1))
  .on("click", function() { zoom(root); });
//zoom in to focus on a particular node
zoomTo([root.x, root.y, root.r * 2]);
//zoom handler
function zoom(d) {
  var focus0 = focus; focus = d;
  //transition animation
  var transition = d3.transition()
    .duration(d3.event.altKey ? 7500 : 750)
    .tween("zoom", function(d) {
      var i = d3.interpolateZoom(view, [focus.x, focus.y, focus.r * 2]);
      return function(t) { zoomTo(i(t)); };
    });
  transition.selectAll("text")
      .filter(function(d) { return d.parent === focus || this.style.display === "inline"; })
        .style("fill-opacity", function(d) { return d.parent === focus ? 1 : 0; })
        .each("start", function(d) { if (d.parent === focus) this.style.display = "inline"; })
        .each("end", function(d) { if (d.parent !== focus) this.style.display = "none"; });
  //hide the wiki article for now.
  $("div").hide();
  //set the header text to the current node name
  $("#header").html(d.name);
  //check if the node clicked has children (i.e. is it a leaf node?)
  if(!d.children) {
    //load an appropriate wiki article for the detailed leaf display on this node.
    $('#article').wikiblurb(
	  {
  		wikiURL: "http://en.wikipedia.org/",
  		apiPath: 'w',
  		section: 0,
  		page: d.name,
  		removeLinks: false,
  		type: 'all',
  		customSelector: ''
	  });
    //make the wiki article appear only once the transition animation is finished
	   setTimeout(function(){$("div").show()}, 750);
    }
  }
  //zoom resizer
  function zoomTo(v) {
    var k = diameter / v[2]; view = v;
    node.attr("transform", function(d) { return "translate(" + (d.x - v[0]) * k + "," + (d.y - v[1]) * k + ")"; });
    circle.attr("r", function(d) { return d.r * k; });
  }
});
//set the height based on diameter
d3.select(self.frameElement).style("height", diameter + "px");
//load a default wiki article
$(document).ready(function()
{
	$('#article').wikiblurb(
	{
		wikiURL: "http://en.wikipedia.org/",
		apiPath: 'w',
		section: 0,
		page: 'Free software',
		removeLinks: false,
		type: 'all',
		customSelector: ''
	});
});
//set up fancy scroll bars on wiki article
$(document).ready(function(){
  $('#article').tinyscrollbar();
});
