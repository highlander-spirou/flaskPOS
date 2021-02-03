// const data =
//   [ { a: 1, b: 1 }
//   , { a: 2, b: 2, c: { d: [ { e: 2 } ] } }
//   , { a: 3, b: { c: { d: { e: { f: 3 } } } } }
//   ]

const deepFind = (f, obj = {}) =>
{ if (Object (obj) === obj)
  { if (f (obj) === true)
      return obj

    for (const [ k, v ] of Object.entries (obj))
    { const res =
        deepFind (f, v)

      if (res !== undefined)
        return res
    }
  }

  return undefined
}


// console.log
//   ( deepFind (x => x.a === 1, data)             // { a: 1, b: 1 }
//   , deepFind (x => x.e === 2, data)             // { e: 2 }
//   , deepFind (x => Array.isArray(x.d), data)    // { d: [ { e: 2 } ] }
//   , deepFind (x => x.f === 3, data)             // { f: 3 }
//   , deepFind (x => x.e && x.e.f === 3, data)    // { e: { f: 3 } }
//   , deepFind (x => x.z === 9, data)             // undefined
//   )