Zepto(function($) {
	$(document)
	  .on('mouseenter', '[data-detail-src]', function() {
	  	this.src = $(this).data('detailSrc');
	  })
	  .on('mouseleave', '[data-detail-src]', function() {
	  	this.src = $(this).data('src');
	  });

  // Pre-load detail images so the first rollover isn't delayed
  $('[data-detail-src]').forEach(function(item) {
  	$('<img/>')[0].src = $(item).data('detailSrc');
  });
});
