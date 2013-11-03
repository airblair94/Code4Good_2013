<!--[if lt IE 9]><script language="javascript" type="text/javascript" src="../dist/excanvas.js"></script><![endif]-->
<script language="javascript" type="text/javascript" src="../dist/jquery.min.js"></script>
<script language="javascript" type="text/javascript" src="../dist/jquery.jqplot.min.js"></script>
<link rel="stylesheet" type="text/css" href="../dist/jquery.jqplot.css" />

$.jqplot('#chart',  [[[1, 2],[3,5.12],[5,13.1],[7,33.6],[9,85.9],[11,219.9]]],
{ title:'Exponential Line',
  axes:{yaxis:{min:-10, max:240}},
  series:[{color:'#5FAB78'}]
});
