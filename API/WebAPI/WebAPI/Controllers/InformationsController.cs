using System.Collections.Generic;
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
        // GET: api/informations
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { GetDB.ConvertDataTableToString(GetDB.GetAll("information")) };
        }

        // GET api/informations/5
        [HttpGet("{username}/{password}")]
        public string Get(string username, string password)
        {
            // Exist
            if(GetDB.GetWithInfo(new List<dynamic>{ "Username", "Password" }, new List<dynamic>{ "16", "ductrong", "123123", "admin@hotmail.com", null }, new List<dynamic>{ "ID", "Username", "Password", "Email", "IsActive" }, "information"))
            {
                return "true";
            }
            return "false";
        }

        // POST api/informations
        [HttpPost]
        public void Post([FromBody]string value)
        {
        }

        // PUT api/informations/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/informations/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
