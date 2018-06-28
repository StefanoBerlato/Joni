function User (id, name, surname, email, categories) {
  this.id = id.toString();
  this.name = name;
  this.surname = surname;
  this.email = email;
  this.categories = [];
  this.errors = [];
}

module.exports = User;
