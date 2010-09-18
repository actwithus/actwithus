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
              , ref: 'mainPanel'
              , width: '100%'
              , title: 'Administration tool'
              })
          , new Ext.ux.ManagedIFramePanel(
              { region: 'east'
              , ref: 'welcomePanel'
              , width: 250
              , title: 'Welcome'
              , collapsible: true
              , split: true
              })
          ]
      });
    viewport.mainPanel.setSrc(document.location + 'admin/');
    viewport.welcomePanel.setSrc(MEDIA_URL + 'site/welcome/index.html');
});
