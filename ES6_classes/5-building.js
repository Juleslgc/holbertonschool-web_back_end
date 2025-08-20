export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && typeof evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    if (typeof sqft !== 'number') {
      throw new TypeError('Sqft must be number');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
