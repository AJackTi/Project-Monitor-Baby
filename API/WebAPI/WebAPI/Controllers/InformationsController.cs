﻿using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using WebAPI.DB;

namespace WebAPI.Controllers
{
    [Route("api/[controller]")]
    public class InformationsController : Controller
    {
        public GetDB getDB;
        public InformationsController()
        {
            getDB = new GetDB();
        }
        // GET: api/values
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { GetDB.ConvertDataTableToString(GetDB.GetAll("test.db")) };
        }

        // GET api/values/5
        [HttpGet("{id}")]
        public string Get(int id)
        {
            return "value";
        }

        // POST api/values
        [HttpPost]
        public void Post([FromBody]string value)
        {
        }

        // PUT api/values/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/values/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
