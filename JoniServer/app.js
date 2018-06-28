// ------------------ Initialization ----------------------

//inspect
var util = require('util');
//express lib
var express = require('express');
var path = require('path');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var exphbs = require('express-handlebars');



// ------------------ Setting up routes ------------------

// Routes
var news = require('./routes/news.js');
var categories = require('./routes/categories.js');
var users = require('./routes/users.js');

//instantiate express
var app = express();

app.set('public', path.join(__dirname, 'views'));
app.engine('handlebars',
    exphbs({defaultLayout: 'main'}));

app.set('view engine', 'handlebars');
var options = { dotfiles: 'ignore', etag: false,
    extensions: ['htm', 'html'],
    index: false
};
// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
//app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname, 'public') , options  ));

app.use('/news', news);
app.use('/categories', categories);
app.use('/users',users);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error',{ error: err.message });
});

module.exports = app;
