async update{{cname}}(data,status){
    const payload = {};
    const obj = JSON.parse(JSON.stringify(data));
    obj['status'] = status;
    console.log({"payload":payload});
    try {
        await store.dispatch('users_secrets/update{{cname}}',payload);
        log_success('{{cname}} updated!');
    } catch(err) {
        log_error(err);
    }
},

