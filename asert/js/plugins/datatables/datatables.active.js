(function ($) {
  "use strict";

  /*Default*/
  if ($(".data-table-default").length) {
    $(".data-table-default").DataTable({
      responsive: true,
      language: {
        paginate: {
          previous: '<i class="zmdi zmdi-chevron-left"></i>',
          next: '<i class="zmdi zmdi-chevron-right"></i>',
        },
      },
    });
  }

  /*Export Buttons*/
  if ($(".data-table-export_2").length) {
    $(".data-table-export_2").DataTable({
      responsive: true,
      dom: "Bfrtip",
      buttons: ["copy", "csv", "excel", "pdf", "print"],
      language: {
        paginate: {
          previous: '<i class="zmdi zmdi-chevron-left"></i>',
          next: '<i class="zmdi zmdi-chevron-right"></i>',
        },
      },
    });
  }

  if ($(".data-table-export").length) {
    $(".data-table-export").DataTable({
      // Datatables configurations
      paging: true, // Pagination
      pageLength: 10, // Data per page
      lengthChange: true, // Show entries per page
      autoWidth: true, // Control the auto width on columns
      searching: true, // Input search
      bInfo: true, // Infor on footer
      bSort: true, // Filter A to Z and Z to A
      responsive: false,
      // Disable columns with specific filter A to Z
      //"columnDef": [{
      //    //"targets": 5,
      //    "targets": [4,5],
      //    "orderable": false
      //}]
      dom: 'lBfrtip',
      //buttons: ["copy", "csv", "excel", "pdf", "print"],
      language: {
        paginate: {
          previous: '<i class="zmdi zmdi-chevron-left"></i>',
          next: '<i class="zmdi zmdi-chevron-right"></i>',
        },
      },
      buttons: [
          {   
              extend: 'copy',
              text: 'copy',
              className: 'btn btn-secondary',
              titleAttr: 'Copy',
              exportOptions: {
                columns: [0, 1, 2, 3, 4, 5]
              },
          },
          {
            extend: 'excel',
            text: 'excel',
            className: 'btn btn-secondary',
            titleAttr: 'excel',
            exportOptions: {
              columns: [0, 1, 2, 3, 4, 5]
            },
          },
          {
            extend: 'pdf',
            text: 'pdf',
            className: 'btn btn-secondary',
            titleAttr: 'PDF',
            exportOptions: {
              columns: [0, 1, 2, 3, 4, 5]
            },
            tableHeader: {
              alignment: 'center'
            },
            //customize: function (doc) {
              //doc.style.tableHeader.alignment = 'center'; // Header position
              //doc.style.tableBodyOdd.alignment = 'center'; // Body position 1 (grey)
              //doc.style.tableBodyEven.alignment = 'center'; // Body position 1 (white)
              //doc.style.tableHeader.fontSize = 7; // Header font-size
              //doc.defaultStyle.fontSize = 6; // Body font-size
              // To get 100% width of the table
              //doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('');
            //},
          },
          {
            extend: 'print',
            text: 'print',
            className: 'btn btn-secondary',
            titleAttr: 'print',
            exportOptions: {
              columns: [0, 1, 2, 3, 4, 5]
            },
            customize: function (win) {
              $(win.document.body).css('font-size','10pt'),
              $(win.document.body).find('table')
                .addClass('compact')
                .css('font-size', 'inherit');
            }
          },
      ]
  });
  }
})(jQuery);
