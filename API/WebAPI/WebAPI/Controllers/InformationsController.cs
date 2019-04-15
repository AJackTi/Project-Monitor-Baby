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

        // GET api/informations/username/password
        [HttpGet("{username}/{password}")]
        public string Get(string username, string password)
        {
            // Exist
            if(GetDB.GetWithInfoExactly(new List<dynamic>{ "Username", "Password" }, new List<dynamic>{ username, password }, new List<dynamic>{ "Username", "Password" }, "information"))
            {
                return "true";
            }
            return "false";
        }

        // POST api/informations/username/password
        [HttpPost("{username}/{password}")]
        public JsonResult Post(string username, string password)
        {
            if (GetDB.GetWithInfoExactly(new List<dynamic> { "Username", "Password" }, new List<dynamic> { username, password }, new List<dynamic> { "Username", "Password" }, "information"))
            {
                return Json("false");
            }
            if (!PostDB.PostInfo(new List<dynamic> { username, password }, new List<dynamic> { "Username", "Password" }, "information"))
            {
                return Json("false");
            }
            return Json("true");
        }

        // PUT api/informations/username/passwors
        [HttpPut("{username}/{password}")]
        public void Put(string username, string password)
        {

        }

        // DELETE api/informations/username/password
        [HttpDelete("{username}/{password}")]
        public void Delete(string username, string password)
        {

        }
    }
}
