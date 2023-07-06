$(document).ready(function () {
  const Species = {};
  const lst = Object.values(Species);
});
function appendText (text, elementId) {
  const targetElement = document.getElementById(elementId);

  if (targetElement) {
    const textNode = document.createTextNode(text);
    targetElement.appendChild(textNode);
  } else {
    console.error(`Element with ID "${elementId}" not found.`);
  }
}
const target = document.getElementById('ailment');
const pmButton = document.getElementById('powderyMildew');
const powMil = `
    <h2>Powdery Mildew</h2>
    <img src="../static/images/powderyMIldew.jpeg" alt="pmil image">
    <p> Powdery mildew is a fungal disease that affects many plants, flowers, vegetables and fruits. Powdery mildew is an easy one to identify. Infected plants will display a white powdery substance that is most visible on upper leaf surfaces, but it can appear anywhere on the plant including stems, flower buds, and even the fruit of the plant.  This fungus thrives during low soil moisture conditions combined with high humidity levels on the upper parts of the plant surface.  It tends to affect plants kept in shady areas more than those in direct sun. It affects a number of plants, including lilacs, apples, grapes, cucumbers, peas, phlox, daisies and roses.
Rake up and destroy infected leaves to reduce the spread of spores. Also, give plants good drainage and ample air circulation. Avoid overhead watering at night; mid-morning is preferred to allow foliage to dry before evening. Commercial fungicides are available for powdery mildew, or you can spray with a solution of one tsp. baking soda and one quart of water
    </p>
    `;
window.onload=function(){  
  pmButton.addEventListener('click', () => {
    appendText(powMil, target);
  });
};
