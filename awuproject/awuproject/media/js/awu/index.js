Ext.onReady(function () {
    // Create viewport across entire browser window.
    var viewport = new Ext.Viewport(
      { layout: 'border'
      , items:
          [ new Ext.BoxComponent(
              { region: 'north'
              , height: 32
              })
          , new Ext.ux.ManagedIFramePanel(
              { region: 'center'
              , ref: 'mifp'
              , width: '100%'
              , title: 'Administration tool'
              })
          ]
      });
    viewport.mifp.setSrc(document.location + 'admin/');
});
