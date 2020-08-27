set{{cname}}(state,data) {
    const objects = {};
    for (let i = 0; i < data.length; i++) {
        const obj = data[i];
        objects[obj._id] = obj;
    }

    state.{{name}} = objects;
},
